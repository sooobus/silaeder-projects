import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from flask import Flask
app = Flask(__name__)
from flask import render_template, request, redirect, url_for
from Ornament_group import game
import os
from werkzeug.utils import secure_filename
# configuration
DATABASE = 'projects.db'
#DEBUG = True
#SECRET_KEY = 
#USERNAME = 
#PASSWORD = 

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route("/")
def hello():
    cur = g.db.execute('select * from entries order by id desc')
    entries = [dict(uid=row[0], title=row[1], text=row[2], author=row[3], supervisor=row[4], image_url=row[5], url=row[6]) for row in cur.fetchall()]
    print(entries)
    return render_template('hello-boot.html', entries=entries)

def use():
    global name, number, UPLOAD_FOLDER, ALLOWED_EXTENSIONS
    name = 200
    number = '20'

    UPLOAD_FOLDER = ''
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp', 'webp'])

    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/projects/ornament_group/")
def ornament():
    use()
    return render_template('ornament_group.html')
@app.route("/make", methods = ['GET', 'POST'])
def do1():
    if request.method == 'GET':
        return render_template("ornament_group.html", word = 'make')
@app.route("/guess", methods = ['GET', 'POST'])
def do2():
    if request.method == 'GET':
        return render_template("ornament_group.html", word = 'guess')
def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
@app.route("/image", methods = ['GET', 'POST'])
def do3():
        use()
        global name
        global number
        if request.method == "POST":
                word = ''
                try:
                    import os
                    os.remove('static/'+str(name)+'.jpg')
                except:
                    None
                try:
                    number = request.form["num"]
                    word = 'make'
                except:
                    word = 'guess'
                    from random import randint
                    number = randint(1,17)
                    number = str(number)
                file = request.files['file']
                file.filename = 'image.jpg'
                if file and allowed_file(file.filename):
                    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    if number in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17']:
                        name += 1
                        game(number, filename, name)
                    else:
                        number = '0'
                    if word == "guess":
                        return render_template("ornament_group.html", name = name, number = number, word = word)
                    else:
                        return render_template("ornament_group.html", name = name, number = number, word = "m")
@app.route("/check", methods = ['GET', 'POST'])
def do4():
    global number
    if request.method == "POST":
        ans = request.form["ans"]
        if ans == number:
            return render_template("ornament_group.html", text = 'You are right!')
        else:
            return render_template("ornament_group.html", text = 'It was group number', number = number)
@app.route("/students/")
def show_students_call():
    return render_template('students.html')

@app.route("/advisors/")
def show_advisors_call():
    return render_template('students.html')




if __name__ == '__main__':
    app.run()
