# 导入topic_app蓝图程序用于声明路由
from app.topic import topic_app
from flask import render_template


@topic_app.route("/")
def topic_index():
    return render_template("index.html")
