import re
import time
import base64
import hmac


def isPhone(phone):
    if phone is  None:
        return False    
    return re.match(r"^1[356789]\d{9}$", phone) == None


def make_token(key, expire=60):
    """
    通过hmac sha1 算法产生用户给定的key和token的最大过期时间戳的一个消息摘要，
    将这个消息摘要和最大过期时间戳通过":"拼接起来，再进行base64编码，生成最终的token
    @Args:
        key: str (用户给定的key，需要用户保存以便之后验证token,每次产生token时的key 都可以是同一个key)
        expire: int(最大有效时间，单位为s)
    @Return:
        state: str
    """
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshex_str = hmac.new(key.encode("utf-8"), ts_byte, 'sha1').hexdigest()
    token = ts_str+':'+sha1_tshex_str
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))

    return b64_token.decode("utf-8")

def certify_token(key, token):
    """
    将token进行base64解码,通过token得到token最大过期时间戳和消息摘要。判断token是否过期。
    如没过期才将 从token中的取得最大过期时间戳进行hmac sha1 算法运算(注意这里的key要与产生token的key要相同)，
    最后将产生的摘要与通过token取得消息摘要进行对比， 如果两个摘要相等，则token有效，否则token无效 。
    @Args:
        key: str
        token: str
    @Returns:
        boolean
    """
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return False
    ts_str = token_list[0]
    if float(ts_str) < time.time():
        return False
    known_sha1_tsstr = token_list[1]
    sha1 = hmac.new(key.encode("utf-8"), ts_str.encode('utf-8'), 'sha1')
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != known_sha1_tsstr:
        # token certification failed
        return False
    # token certification success
    return True