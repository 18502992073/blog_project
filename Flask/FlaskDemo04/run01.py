from flask import Flask, request, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import or_, func
import pymysql
import math
pymysql.install_as_MySQLdb()
# 以上两句在flask中可以在mysql后用+pymyql代替

app = Flask(__name__)

# 连接到mysql中falskDB数据库
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "mysql://root:123456@127.0.0.1:3306/flaskDB"

# 指定不使用信号追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 指定程序启动模式为调试模式
app.config['DEBUG'] = True

# 执行完增删改之后的自动提交
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True

# 创建SQLAlchemy的实例
db = SQLAlchemy(app)

# 创建Manage对象并指定要管理的app
manager = Manager(app)

# 创建Migrate对象，并指定关联的app和db
migrate = Migrate(app, db)

# 为manage添加数据库迁移指令
# 为manage增加一个子命令-db(自定义)具体操作由MigrateCommand来提供
manager.add_command('db', MigrateCommand)


class Users(db.Model):
    """
    创建实体类Users,映射到数据库中叫users表
    创建字段id，主键，自增
    创建字段usernamr，长度为80的字符串，不能为空，值唯一，加索引
    创建字段age，整数，允许为空
    创建字段email，长度为120字符串，必须唯一
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True, index=True)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(120), unique=True)
    isActive = db.Column(db.Boolean, default=True)
    birthday = db.Column(db.Date)

    def __repr__(self):
        return "<User %r>" % self.username


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30), nullable=False)
    sage = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer, nullable=False)
    # 增加一个外键列course_id，引用自Course类
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30))
    # 增加对Teacher的关联属性和反向引用关系属性
    course_teachers = db.relationship(
        "Teacher",
        backref="teacher_course",
        lazy="dynamic"
    )


class Wife(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wname = db.Column(db.String(30))
    # 增加birthday
    birthday = db.Column(db.Date)
# 删除所有表结构
# db.drop_all()
# 将所有的实体类生成对应的表结构，前提：表不存在的情况下才能生成
# db.create_all()


@app.route('/01-add')
def add_views():
    # 1.创建Users的对象并赋值
    user = Users()
    user.username = "qtx"
    user.age = 30
    user.email = "qtx.qi@163.com"
    user.birthday = "1999-10-12"
    # 2.将Users的对象保存回数据库
    db.session.add(user)
    # 3.提交事务
    # db.session.commit()
    # 4.响应
    return "提交成功"


@app.route('/02-reg', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template("regist.html")
    else:
        user = Users()
        user.username = request.form['uname']
        user.age = request.form['uage']
        user.email = request.form['uemail']
        user.birthday = request.form['ubirthday']
        if 'stat' not in request.form:
            user.isActive = False
        db.session.add(user)
        return "注册成功"


@app.route('/03-query')
def query():
    # 查询Users实体中的id，username两列值
    # query = db.session.query(Users.id, Users.username)
    # print(query)
    # print("type", type(query))
    # return "查询数据成功"

    # 查询Users实体中所有数据
    # users = db.session.query(Users).all()
    # for u in users:
    #     print(u.id)
    # return "查询数据成功"

    # 3.查询Users实体中的第一条数据
    # first = db.session.query(Users).first()
    # print(first)
    # return "查询数据成功"

    # 4.查询Users实体中共有多少条数据
    count = db.session.query(Users).count()
    return "共有%d条数据" % count


@app.route('/04-filter')
def filter_views():
    # 1.查询年龄大于30的users的信息
    res = db.session.query(Users).filter(Users.age >= 30).all()
    print(res)

    # 2.查询id为2的users的信息
    res = db.session.query(Users).filter(Users.id == 2).first()
    print(res)

    # 3.查询isActive为True并且年龄大于30的users的信息
    # 方案一：使用多filter()函数
    res = db.session.query(Users).filter(Users.isActive == True)\
        .filter(Users.age >= 30).all()
    print(res)
    # 方案二：使用filter(条件1,条件2)函数
    res = db.session.query(Users).filter(Users.isActive == True, Users.age >= 30).all()
    print(res)

    # 4.查询isActive为True或者年龄大于30的users的信息
    # or：使用or_函数
    # from sqlalchemy import or_
    res = db.session.query(Users).filter(
        or_(Users.isActive == True, Users.age >= 30)).all()
    print(res)

    # 5.查询email中包含i的users的信息
    # sql：select * from users where email like '%i%'
    # 模糊查询like，需要使用实体类属性提供的like()完成查询
    res = db.session.query(Users).filter(Users.email.like('%i%')).all()

    # 6.查询年龄是30,或17或45岁的Users的信息
    # 模糊查询in 需要使用实体类属性提供in_函数完成
    res = db.session.query(Users).filter(
        Users.age.in_([30, 17, 45])).all()
    print(res)

    # 7.查询年龄在18到35之间的Users的信息
    # 模糊查询between..and.. 需要使用实体类属性提供between(值1,值2)完成查询
    res = db.session.query(Users).filter(Users.age.between(18, 35)).all()
    print(res)
    return "执行查询过滤器函数成功"


@app.route('/05-users')
def users_views():
    res = db.session.query(Users).filter(Users.isActive == True)
    if 'kw' in request.args:
        kw = request.args['kw']
        res = res.filter(
            or_(
                Users.username.like('%'+kw+'%'),
                Users.email.like('%'+kw+'%')
            )
        )
    res = res.all()
    return render_template("05-users.html", request=locals())


@app.route('/06-limit')
def limit_views():
    users = db.session.query(Users).limit(2).offset(2).all()
    print(users)
    return "查询成功"


@app.route('/07-page')
def page_view():
    # 每页显示记录数量
    page_size = 2
    # 当前页
    current_page = int(request.args.get('current_page', "1"))
    ost = (current_page-1)*page_size
    # 查询第current_page页数据
    users = db.session.query(Users).offset(ost).limit(page_size).all()

    # 通过page_size和总记录数计算尾页页码
    total_count = db.session.query(Users).count()
    last_page = math.ceil(total_count/page_size)

    # 计算上一页页码
    prev_page = 1
    if current_page > 1:
        prev_page = current_page - 1

    # 计算下一页页码
    next_page = last_page
    if current_page < last_page:
        next_page = current_page + 1
    return render_template('07-page.html', params=locals())


@app.route('/08-aggr')
def aggregat_views():
    # 查询Users实体中所有人的平均年龄
    res = db.session.query(func.avg(Users.age)).all()
    print("平均年龄%2f" % res[0][0])
    # 查询Users实体中所有人的平均年龄,总年龄，最大最小年龄，总人数
    res = db.session.query(
        func.avg(Users.age),
        func.sum(Users.age),
        func.max(Users.age),
        func.min(Users.age),
        func.count(Users.id)
    ).all()
    print(res)
    return "聚合函数查询成功"


@app.route('/09-aggr-exer')
def aggr_exer():
    res = db.session.query(func.avg(Users.age)).filter(Users.age > 18).all()
    print(res)
    res = db.session.query(Users.isActive, func.count(Users.id)).group_by('isActive').all()
    print(res)
    res = db.session.query(Users.isActive, func.count(Users.id)).group_by('isActive')\
        .having(func.count(Users.id) > 2).all()
    print(res)
    res = db.session.query(Users.isActive, func.count(Users.id)).filter(Users.age > 18)\
        .group_by('isActive').having(func.count(Users.id) > 2).all()
    print(res)
    res = db.session.query(Users).filter(Users.age > db.session.query(Users.age)
                                         .filter(Users.username == "qqq")).all()
    print(res)
    return "聚合函数查询成功"


@app.route('/10-update')
def update_views():
    # 修改qqq的isActive属性为True
    user = db.session.query(Users).filter_by(username='qqq').first()
    user.isActive = False
    db.session.add(user)
    # user = db.session.query(Users).filter_by(id=6).first()
    # db.session.delete(user)
    return "ok"


@app.route('/11-upuser', methods=['GET', 'POST'])
def upuser():
    if request.method == 'GET':
        # 接收id
        id = request.args['id']
        # 按id查对象
        user = db.session.query(Users).filter_by(id=id).first()
        # 将对象发送到模板上
        return render_template('11-upuser.html', user=user)
    else:
        id = request.form['id']
        user = db.session.query(Users).filter_by(id=id).first()
        user.username = request.form['uname']
        user.age = request.form['uage']
        user.email = request.form['uemail']
        user.birthday = request.form['ubirthday']
        if 'stat' not in request.form:
            user.isActive = False
        else:
            user.isActive = True
        db.session.add(user)
        flash("修改成功")
        return redirect('/05-users')


@app.route('/12-regtea')
def regtea():
    # 1.通过teacher对象的course_id属性插入关联的数据
    # teaQi = Teacher()
    # teaQi.tname = "QTX"
    # teaQi.tage = 30
    # teaQi.course_id = 1
    # db.session.add(teaQi)
    # 2.通过teacher对象的course属性插入关联数据
    # 2.1查询出python高级
    course = Course.query.filter_by(cname="python高级").first()
    print(course)
    # 2.2声明tea对象，并关联查询出的course对象
    tea = Teacher()
    tea.tname = "吕小小泽"
    tea.tage = 28
    tea.teacher_course = course  # 底层是将course.id给了tea.course_id属性
    db.session.add(tea)
    return "ok"


if __name__ == "__main__":
    # app.run(debug=True)
    # 启动服务的操作交给manage来管理
    manager.run()
