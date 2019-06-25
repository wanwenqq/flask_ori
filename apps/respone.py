from flask import abort
from flask import  jsonify

class ResponseCode:
    SUCCESS = 200
    WRONG_PARAM = 400  #对400进行处理
    MESSAGE = '处理成功！'


def make_respone(data=None, message=ResponseCode.MESSAGE, status=ResponseCode.SUCCESS):
    return jsonify({
        'message': message,
        'status': status,
        'data': data
    })


def my_abort(http_status_code, *args, **kwargs):
    if http_status_code == 400:
        # 重定义400返回参数
        # print(args)
        # print(kwargs)
        abort(400, **make_respone(data=[kwargs.get('message')], message='请求接口有错误！', status=http_status_code))

    abort(http_status_code)
