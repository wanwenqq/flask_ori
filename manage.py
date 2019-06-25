from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from exts import db
from apps.v1 import models as v1_models

manager = Manager(app)

Migrate(app, db)
manager.add_command('db', MigrateCommand)

v1_user = v1_models.User

@manager.option('-c','--phone',dest='phone')
@manager.option('-p','--password',dest='password')
@manager.option('-u','--username',dest='username')
def m_create_user(username,password,phone):
    user = v1_user(phone=phone,password=password,username=username)
    db.session.add(user)
    db.session.commit()
    print('创建用户成功')


if __name__ == '__main__':
    manager.run()