from flask import Flask
app = Flask(__name__)
from flask import render_template, request, redirect, url_for
from Ornament_group import game
import os
from werkzeug.utils import secure_filename
@app.route("/")
def main():
        return render_template('ornament_group.html')

def allowed_file(filename):
        return '.' in filename and \
                filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
@app.route("/make", methods = ['GET', 'POST'])
def make():
        if request.method == 'GET':
                return render_template("ornament_group.html", word = 'make')

@app.route("/guess", methods = ['GET', 'POST'])
def guess():
        if request.method == 'GET':
                return render_template("ornament_group.html", word = 'guess')
@app.route("/image", methods = ['GET', 'POST'])
def image():
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
                        print(number)
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
def check():
        if request.method == "POST":
                ans = request.form["ans"]
                if ans == number:
                        return render_template("ornament_group.html", text = 'You are right!')
                else:
                        return render_template("ornament_group.html", text = 'It was group number', number = number)
if __name__ == '__main__':
        app.run()
