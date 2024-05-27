# 青韵瓷器前端+论坛功能

本项目是投机设失败的项目，但是是辛辛苦苦做了好久的所以投一下纪念一下。

因为不太了解flask所以用了一体化设计。

本项目前端使用一些bootsharp等，后端使用flask框架，有账号注册，账号登录，发帖功能，为了赶项目发帖页面有很多虚的东西，可以后续完善，但发帖功能完善

如果下载使用，后端数据库配置在config.py文件

```python
# MySQL所在的主机名
HOSTNAME = "127.0.0.1"
# MySQL监听的端口号，默认3306
PORT = 3306
# 连接MySQL的用户名
USERNAME = "root"
# 连接MySQL的密码
PASSWORD = "password"
# MySQL上创建的数据库名称
DATABASE = "culture"
DB_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI = DB_UR
```

将password改为自己数据库密码，并且创建culture数据库，且在mysql中创建以下表

```mysql
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(200) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    join_time DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE email_captcha (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    captcha VARCHAR(10) NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE question (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE answer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    question_id INT,
    author_id INT,
    FOREIGN KEY (question_id) REFERENCES question (id),
    FOREIGN KEY (author_id) REFERENCES user (id)
);
```

在config文件下面还需要配置发送邮箱的参数

```python
# 邮箱配置
MAIL_SERVER = "smtp.163.com"   #项目中用163邮箱
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True   #发送邮件会提示日志信息
MAIL_USERNAME = "XXXXXXXXX@163.com"
MAIL_PASSWORD = "XXXXXXXXXXXX"  #登录邮箱——>设置——>账号——>POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务——>获取授权码
MAIL_DEFAULT_SENDER = "XXXXXXXXXXX@163.com"
```

在user.py可以修改邮件发送内容

```python
message = Message(
            subject="邮箱主题",
            recipients=[email],
            body=f"【青韵论坛】您的注册码是：{captcha}，请不要告诉任何人哦！"
        )
```

最后在app.py文件运行
