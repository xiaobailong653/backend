1、创建超级用户
# python manage.py createsuperuser
admin       wjsbgsn653

2、创建app
# python manage.py startapp {appname}

3、创建数据库
$ python manage.py migrate   # 创建表结构

$ python manage.py makemigrations union  # 让 Django 知道我们在我们的模型有一些变更
$ python manage.py migrate union   # 创建表结构

4、创建数据库
CREATE DATABASE IF NOT EXISTS backend DEFAULT CHARSET utf8 COLLATE utf8_general_ci;

5、创建静态文件
python manage.py collectstatic
