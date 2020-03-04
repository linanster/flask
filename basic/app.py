from os import path
import os

from flask import Flask, request, url_for, redirect, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        basepath = path.abspath(path.dirname(__file__))
        upload_path = path.join(basepath, 'static\\uploads')
        file = request.files['file1']
        filename = path.join(upload_path, secure_filename(file.filename))
        print(filename)
        # file.save(filename)
        file.save("C:\\\Users\\\linan\\\PycharmProjects\\basic\static\\uploads\\temp.txt")

        return redirect(url_for('upload'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()
