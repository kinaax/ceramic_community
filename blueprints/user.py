from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session, flash
from exts import mail
from flask_mail import Message
from models.models import EmailCaptchaModel, UserModel
import string
import random
from exts import db
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/login", methods=['GET', 'POST'])
def login():    # 登录
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        form = LoginForm(request.form)  # 存储前端表单的内容
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                return redirect("/")
            else:
                flash("邮箱和密码不匹配！")
                return redirect(url_for("user.login"))
        else:
            flash("格式错误！")
            return redirect(url_for("user.login"))
    else:
        return render_template("login.html")


@user_bp.route("/register", methods=['GET', 'POST'])
def register():    # 注册
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)  # 存储前端表单的内容
        # if form.validate():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        hash_password = generate_password_hash(password)
        user = UserModel(email=email, username=username, password=hash_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user.login"))
        # else:
        #     return redirect(url_for("user.register"))


@user_bp.route("/captcha", methods=['POST'])
def get_captcha():  # 验证码
    email = request.form.get("email")
    letters = string.ascii_letters + string.digits
    captcha = "".join(random.sample(letters, 4))

    if email:
        message = Message(
            subject="邮箱主题",
            recipients=[email],
            body=f"【青韵论坛】您的注册码是：{captcha}，请不要告诉任何人哦！"
        )
        mail.send(message)
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if captcha_model:
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.now()
            db.session.commit()
        else:
            captcha_model = EmailCaptchaModel(email=email, captcha=captcha)
            db.session.add(captcha_model)
            db.session.commit()
            # print("captcha:", captcha)
        # 200 成功、正常的请求
        return jsonify({"code": 200})
    else:
        # 400 客户端错误
        return jsonify({"code": 400, "message": "请先传递邮箱！"})


@user_bp.route("/logout")
def logout():   # 退出登录
    session.clear()
    return redirect(url_for("user.login"))