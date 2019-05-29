from flask import Flask, request, render_template
import datetime, os

app = Flask(__name__)


def generate_filename(filename):
    """
        通过原始文件名生成一个由事件戳来组成的新文件名
    :param filename: 原始文件名
    :return: 新文件名
    """
    ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    ext = file.filename.split('.')[-1]
    filename = ftime + '.' + ext
    return filename


def generate_upload_path(file, dirname, filename):
    """
        生成上传文件路径
    :param file: 获取当前文件的根路径的文件
    :param dirname: 保存文件的具体目录
    :param filename: 保存的文件名
    :return:
    """
    base_dir = os.path.dirname(file)
    upload_path = os.path.join(base_dir, dirname, filename)
    return upload_path


@app.route('/01-file', methods=['GET', 'POST'])
def file_views():
    if request.method == 'GET':
        return render_template("01-file.html")
    else:
        # 1.接收前端传来的图片
        if 'uimg' in request.files:
            file = request.files['uimg']
            # 2.拼年月日十分秒微妙作为文件名
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            # 3.获取上传文件的扩展名
            ext = file.filename.split('.')[-1]
            filename = ftime + '.' + ext
            # 准备上传路径
            basedir = os.path.dirname(__file__)
            print("basedir:", basedir)
            # 拼上传的完整路径
            upload_path = os.path.join(basedir, "static", filename)
            file.save(upload_path)
            return "上传成功"


@app.route("/02-file", methods=['GET', 'POST'])
def file():
    if request.method == 'GET':
        return render_template("02-file-exer.html")
    else:
        titel = request.form['btitel']
        type = request.form['btype']
        content = request.form['bcontent']
        # 1.接收前端传来的图片
        if 'uimg' in request.files:
            file = request.files['uimg']
            filename = generate_filename(file)
            upload_path = generate_upload_path(__file__, 'static/upload', filename)
            file.save(upload_path)
            print(titel)
            print(type)
            print(content)
            print(filename)
            return "上传成功"


if __name__ == "__main__":
    app.run(debug=True)
