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
SQLALCHEMY_DATABASE_URI = DB_URL

# 邮箱配置
MAIL_SERVER = "smtp.163.com"   #项目中用QQ邮箱
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True   #发送邮件会提示日志信息
MAIL_USERNAME = "18170405605@163.com"
MAIL_PASSWORD = "RFAYPDRIYUCWVBCI"  #登录qq邮箱——>设置——>账号——>POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务——>获取授权码
MAIL_DEFAULT_SENDER = "18170405605@163.com"

# 应用中使用 Flask-Session 等会话扩展时，需要设置一个随机的密钥，以防止会话数据被篡改。
# 可以在 Flask 应用的配置参数中添加 SECRET_KEY 变量，并设定一个复杂的随机字符串作为密钥
SECRET_KEY = 'a random string'