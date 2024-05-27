from flask import Flask, session, g
import config
from exts import db, mail
from models.models import UserModel
from flask_migrate import Migrate
from blueprints.qa import qa_bp
from blueprints.user import user_bp

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
mail.init_app(app)

app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)

migrate = Migrate(app, db)

# 流程：请求——>before_request——>视图函数——>视图函数返回模板——>context_processor
@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            # 给g绑定一个叫做user的变量
            # setattr(g,"user",user)
            # 全局变量
            g.user = user
        except:
            g.user = None


@app.context_processor
def context_processor():
    if hasattr(g, "user"):
        return {"user": g.user}
    else:
        return {}


if __name__ == '__main__':
    app.run(debug=True)
