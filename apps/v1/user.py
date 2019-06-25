from flask import views,Blueprint,request,jsonify
from utils import common
from .models import User
from apps.respone import make_respone
from utils.redistool import RedisCache
from exts import db
from apps.decorators import login_required
import config

bp = Blueprint('cms', __name__, url_prefix='/v1')

class BaseView(views.MethodView):
    def __init__(self):
        super().__init__()

class UserView(BaseView):
    def get(self):
        return '登录成功'

    def post(self):
        userid = request.values.get('userid')
        return '登录成功'


class LoginView(BaseView):
    def __init__(self):
        self.respone = {
            'id':None,
            'phone':None,
            'token':None
        }
    def post(self):
        phone = request.values.get('phone')
        password = request.values.get('password')
        if common.isPhone(phone) or password is None:
            # return make_respone(data={},message='用户名或密码错误',status=601)
            return make_respone(None,400,'用户名或密码错误')
        else:            
            user  = User.query.filter_by(phone=phone).first()
            if user and user.check_password(password):
                # 根据userid生成token,并返回给前端
                token = common.make_token(str(config.TOKEN_KEY))
                self.respone['id'] = user.id
                self.respone['phone'] = user.phone
                self.respone['token'] = token
                # 在redis中记录token的值
                # RedisCache().set_data(user.id, token)
                # 返回登录成功包
                return make_respone(self.respone, 200, '登录成功')
            else:
                return make_respone(None, 403, '登录失败')

class RegisterView(BaseView):

    def __init__(self):
        self.respone = {
            'id':None,
            'phone':None,
            'token':None
        }

    def post(self):
        phone = request.values.get('phone')
        password = request.values.get('password')
        if common.isPhone(phone) or password is None:
            return make_respone(None,400,'用户名或密码设置错误')
        else:
            user =  User(username='bookan1',phone=phone,password=password)
            try:
                db.session.add(user)
                db.session.commit()
                return make_respone(None,200,'注册成功')
            except Exception as e:
                print(e)
                return make_respone(None,600,'注册失败')


bp.add_url_rule(rule='/register/',view_func=RegisterView.as_view('register'))
bp.add_url_rule(rule='/login/',view_func=LoginView.as_view('login'))
bp.add_url_rule(rule='/user/',view_func=UserView.as_view('user'))

@bp.route('/')
@login_required
def index():
    # key = '18602736775'
    # token = common.make_token(key,1)
    # print(token)
    # isok = common.certify_token(key,token)
    # print(isok)
    # return 'user index'
    return make_respone()