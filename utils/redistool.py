import redis
import config

# 测试用
# def operator_status(func):
#   def gen_status(*args, **kwargs):
#     error, result = None, None
#     try:
#       result = func(*args, **kwargs)
#     except Exception as e:
#       error = str(e)
#     return {'result': result, 'error': error}
#   return gen_status

class RedisCache(object):
  def __init__(self):
    if not hasattr(RedisCache, 'pool'):
      RedisCache.create_pool()
    self._connection = redis.Redis(connection_pool = RedisCache.pool)

#   @staticmethod
  def create_pool():
    RedisCache.pool = redis.ConnectionPool(
        host = config.REDIS_HOST,
        port = config.REDIS_PORT,
        db  = config.REDIS_DB)

#   @operator_status
  def set_data(self, key, value):
    return self._connection.set(key, value)

#   @operator_status
  def get_data(self, key):
    return self._connection.get(key)

#   @operator_status
  def del_data(self, key):
    return self._connection.delete(key)