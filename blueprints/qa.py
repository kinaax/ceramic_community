from flask import Blueprint, render_template, request, g, redirect, url_for, flash
from decorators import login_required
from exts import db
from .forms import QuestionForm,AnswerForm
from models.models import QuestionModel, AnswerModel
from sqlalchemy import or_

qa_bp = Blueprint("qa", __name__, url_prefix="/")

@qa_bp.route("/")
def index():
    return render_template("start.html")

@qa_bp.route("/community")
def community():
    questions = QuestionModel.query.order_by(db.text("-create_time")).all()
    return render_template("index.html", questions=questions)

@qa_bp.route("/zhu")
def zhu():
    return render_template("index copy.html")

@qa_bp.route("/h1")
def h1():
    return render_template("history1.html")

@qa_bp.route("/h3")
def h3():
    return render_template("history3.html")

@qa_bp.route("/h2")
def h2():
    return render_template("history_2.html")

@qa_bp.route("/por")
def por():
    return render_template("porcelains.html")

@qa_bp.route("/question/public", methods=['GET', 'POST'])
@login_required  # 装饰器
def public_question():
    # 判断是否登录，没有登录，跳转到登录页面
    if request.method == 'GET':
        return render_template("public_question.html")
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect("/")
        else:
            flash("标题或内容格式错误！")
            return redirect(url_for("qa.public_question"))


@qa_bp.route("/question/<int:question_id>")
def question_detail(question_id):
    question = QuestionModel.query.get(question_id)
    return render_template("detail.html", question=question)


@qa_bp.route("/answer/<int:question_id>", methods=['POST'])
@login_required  # 装饰器
def answer(question_id):  # 注册
    form = AnswerForm(request.form)  # 存储前端表单的内容
    if form.validate():
        content = form.content.data
        answer_model = AnswerModel(content=content, author=g.user, question_id=question_id)
        db.session.add(answer_model)
        db.session.commit()
        return redirect(url_for("qa.question_detail", question_id=question_id))
    else:
        flash("请填写评论再提交！")
        return redirect(url_for("qa.question_detail", question_id=question_id))


@qa_bp.route("/search")
def search():
    kword = request.args.get("kword")
    questions = QuestionModel.query.filter(or_(QuestionModel.title.contains(kword),QuestionModel.content.contains(kword))).order_by(db.text("-create_time"))

    return render_template("index.html",questions = questions)

__all__ = ['qa_bp']