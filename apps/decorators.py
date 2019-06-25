from utils.redistool import RedisCache
from functools import wraps
from .respone import make_respone


def login_required(func):
    @wraps(func) # 保留func的属性
    def inner(*args, **kwargs):
        print(args[0].request.value.get('userid'))
        print(kwargs)
        # if 'userid' in session:
        #     return func(*args, **kwargs)
        # else:
        #     #session中没有userid表示没有登录，需要重新登录
        #     return make_respone(None,601,'请重新登录')
        return make_respone()
    return inner