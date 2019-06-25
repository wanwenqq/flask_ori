from utils.redistool import RedisCache

if __name__ == '__main__':
    print (RedisCache().set_data('Testkey', "Simple Test"))