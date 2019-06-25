from flask import Flask,request
import config
from exts import db
from apps.v1 import user_bp
from apps.respone import my_abort,make_respone
from utils.common import certify_token
from apps.ips import ips
from apps.auths import auths

app  = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

app.register_blueprint(user_bp)

@app.route('/')
def index():
    return 'index'

app.abort = my_abort


@app.before_request
def print_request_info():
    # print("请求地址：" + str(request.path))
    # print("请求方法：" + str(request.method))
    # print("---请求headers--start--")
    # print(str(request.headers).rstrip())
    # print("---请求headers--end----")
    # print("GET参数：" + str(request.args))
    # print("POST参数：" + str(request.form))
    print(request.remote_addr)

    #可在此处检查jwt等auth_key是否合法，
    #abort(401)
    #然后根据endpoint，检查此api是否有权限，需要自行处理
    #print(["endpoint",connexion.request.url_rule.endpoint])
    #abort(401)
    #也可做ip检查，以阻挡受限制的ip等
    if filter_request(request):
        return make_respone(None,403,'你被禁了')
    if is_auth_request(request):
        token = request.headers.get('Token',None)
        if not token:
            # 如果 header中没有Token需要重新登录
            return make_respone(None,403,'没有权限，请重新登录')
        else:
            if not certify_token(config.TOKEN_KEY,token):
                # 如果 header中有Token但是校验没有通过
                return make_respone(None,403,'没有权限，请重新登录')

# 非鉴权请求
def is_auth_request(request):
    if request.path in auths:
        return False
    return True
# 过滤IP地址
def filter_request(request):
    if request.remote_addr in ips:
        return True
    return False 


# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.after_request(after_request)


if __name__ == '__main__':
    app.run()