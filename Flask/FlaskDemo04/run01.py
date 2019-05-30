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
    # 增加关联属性和反向引用关系属性，来表示与Course之间的多对多的关系
    # 对Course类和Student类的影响如下：
    # 1.在Student类中会有一个属性叫courses，来表示对student的课程查询
    # 2.在Course类中会有一个属性叫students，来表示对course的学员的查询
    courses = db.relationship(
        "Course",   # 指定多对多的关系中的另一个类
        secondary="student_course",  # 指定第三张关联表名
        lazy="dynamic",  # 要使用courses数据的延迟加载模式
        backref=db.backref(
            "students",  # 加入到Course类中的属性名，表示对Student的查询
            lazy="dynamic"  # 指定在Course中查询student的时候的延迟加载
        )
    )


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer, nullable=False)
    # 增加一个外键列course_id，引用自Course类
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    # 增加一个关联属性，表示要引用的wife信息
    # 关联属性：在Teacher中要增加哪个属性用于表示对Wife的引用
    # 反向引用关系属性：在Teacher中设置但要增加到Wife中，表示的是在Wife中要增加哪个属性表示对Teacher的引用
    wife = db.relationship(
        'Wife',
        backref='teacher',
        uselist=False
    )


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30))
    # 增加对Teacher的关联属性和反向引用关系属性
    teachers = db.relationship(
        "Teacher",
        backref="course",
        lazy="dynamic"
    )


class Wife(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wname = db.Column(db.String(30))
    # 增加birthday
    birthday = db.Column(db.Date)
    # 增加一个属性teacher_id，表示对Teacher类的主键引用，并且增加唯一约束
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), unique=True)


# 创建类StudentCourse，映射到表名：student_course
# 表示Student与Course之间的多对多的第三张关联表
class StudentCourse(db.Model):
    __tablename__ = "student_course"
    id = db.Column(db.Integer, primary_key=True)
    # 外键student_id，引用自student表的主键id
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    # 外键course_id，引用自course表的主键id
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

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
    # 变量-pageSize,表示每页显示的记录数量
    page_size = 2
    # 变量-currentPage,表示当前想看的页数
    current_page = int(request.args.get('current_page', 1))
    # 查询第currentPage页的数据
    # 跳过(currentPage-1)*pageSize条数据,再获取前pageSize条数据
    ost = (current_page - 1) * page_size
    users = db.session.query(Users).offset(ost).limit(page_size).all()

    # 通过pageSize和总记录数计算尾页页码
    total_count = db.session.query(Users).count()
    last_page = math.ceil(total_count / page_size)

    # 计算上一页页码
    # 如果currentPage大于1的话那么上一页就是currentPage-1,否则上一页就是1
    prev_page = 1
    if current_page > 1:
        prev_page = current_page - 1

    # 计算下一页页码
    # 如果currentPage小于lastPage的话那么下一页就是currentPage+1,否则下一页就是尾页
    next_age = last_page
    if current_page < last_page:
        next_page = current_page + 1

    return render_template('07-page.html', params=locals())


# wifes = Wife.query.all()
    # for w in wifes:
    #     p
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
    tea.course = course  # 底层是将course.id给了tea.course_id属性
    db.session.add(tea)
    return "ok"


@app.route('/13-otm', methods=['GET', 'POST'])
def otm():
    if request.method == "GET":
        # 1.查询Course实体类中所有的数据
        courses = Course.query.all()
        # 2.渲染模板
        return render_template('13-otm.html', courses=courses)
    else:
        # 1.接收前端传递过来的数据(tname,tage,cid)
        tname = request.form['tname']
        tage = request.form['tage']
        course_id = request.form['cid']
        # 2.创建Teacher对象并且为属性赋值
        tea = Teacher()
        tea.tname = tname
        tea.tage = tage
        tea.course_id = course_id
        # 3.将tea保存进数据库
        db.session.add(tea)
        return "注册Teacher成功"


@app.route('/14-otm-query')
def otm_query():
    # 通过course对象找到对应的teacher们
    # 1.1查询id为2的course的信息
    # cour = Course.query.filter_by(id=2).first()
    # print("课程名：", cour)
    # # 1.2获取当前course所对应的teacher们
    # teachers = cour.teachers.all()
    # for tea in teachers:
    #     print("姓名：%s，年龄%s" % (tea.tname, tea.tage))

    # 查找qtx所教的课程
    tea = Teacher.query.filter_by(tname="qtx").first()
    cour = tea.course
    print(tea.tname, cour.cname)
    return "ok"


@app.route('/15-otm-exer')
def otm_exer():
    # 1.查询出所有的课程
    courses = Course.query.all()
    # 2.获取前端提交过来的cid参数值，如果没有当0处理
    cid = int(request.args.get('cid', 0))
    # 如果cid的值是0的话，则查询所有老师的信息
    # 如果cid的值非0则按照cid值查找老师信息
    if cid == 0:
        teachers = Teacher.query.all()
    else:
        # 方案1：通过cid到Teacher实体中查询数据
        # teachers = Teacher.query.filter_by(course_id=cid).all()
        # 方案2：通过cid获取课程信息，在通过课程找到对应的老师们
        course = Course.query.filter_by(id=cid).first()
        teachers = course.teachers.all()
    # 4.讲课程和老师渲染到模板中
    return render_template('15-otm-exer.html', params=locals())


@app.route('/16-oto')
def oto_views():
    # 方案1：通过wife对象中的teacher_id属性表示要引用的teacher的主键
    # wife = Wife()
    # wife.wname = '如花'
    # wife.teacher_id = 1
    # db.session.add(wife)
    # 方案2：通过wife对象中的teacher属性表示要引用的teacher对象
    # wife = Wife()
    # wife.wname = '小泽夫人'
    # teacher = Teacher.query.filter_by(tname='吕泽').first()
    # wife.teacher = teacher
    # db.session.add(wife)

    # 3.查询每一名wife所对应的teacher的信息
    wifes = Wife.query.all()
    for w in wifes:
        print("夫人名：%s,老师名：%s" % (w.wname, w.teacher.tname))
    # 4.查询每一名teacher所对应的wife的信息
    # teachers = Teacher.query.all()
    # for tea in teachers:
    #     print("老师名：%s" % tea.tname)
    #     if tea.wife:
    #         print("夫人姓名：%s" % tea.wife.wname)
    #     print("**********")
    return "注册wife成功"


@app.route('/17-mtm')
def mtm_views():
    # 1.增加关联数据
    # sc = StudentCourse()
    # sc.student_id = 1
    # sc.course_id = 1
    # db.session.add(sc)

    # 2.获取小明对象以及python高级对象，再将两个对象关联到一起
    # stu = Student.query.filter_by(sname='小明').first()
    # cour = Course.query.filter_by(cname='python高级').first()
    # # 将cour加入到stu的课程列表中
    # stu.courses.append(cour)

    # 3.小马同学选择了python基础课程
    # stu = Student.query.filter_by(sname='小马').first()
    # cour = Course.query.filter_by(cname='python基础').first()
    # cour.students.append(stu)

    # 4.删除关联数据：通过关联属性反向引用关系属性.remove(实体对象) 实现删除

    # 5.查询小明所选择的课程
    # stu = Student.query.filter_by(sname='小明').first()
    # print("学员名：", stu.sname)
    # print("所选课程：")
    # courses = stu.courses.all()
    # for cour in courses:
    #     print(" 课程名称：", cour.cname)
    
    # 6.查询选修python基础的学员们
    cour = Course.query.filter_by(cname='python基础').first()
    print("课程名：", cour.cname)
    print("学员们：")
    students = cour.students.all()
    for stu in students:
        print(" 学员名：", stu.sname)
    return "ok"


if __name__ == "__main__":
    # app.run(debug=True)
    # 启动服务的操作交给manage来管理
    manager.run()
