DEBUG = True

#MySQL Database
HOST = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
PASSWORD = 'bookan'
DATABASE = 'flaskori'

DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset-utf8'.format(username=USERNAME,
                                                                                        password=PASSWORD,
                                                                                        host=HOST,
                                                                                        port=PORT,
                                                                                        db=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False


#redis db
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0

TOKEN_KEY = '1234567890abcdefghijklmnopqrstuvwxyz~!#$%^&*()'