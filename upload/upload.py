#! /usr/bin/env python
# coding: utf8
#

from os import path, listdir
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
# from werkzeug.wsgi import SharedDataMiddleware

EXT_LIMIT = True
# UPLOAD_FOLDER = 'C:\Users\\212790747\python\upload'
UPLOAD_FOLDER = path.abspath(path.dirname(__file__))
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'ABC'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if EXT_LIMIT and not allowed_file(file.filename):
            return "File extention forbidden!"            
        if file:
            filename = secure_filename(file.filename)
            destfile = path.join(app.config['UPLOAD_FOLDER'], filename)  
            file.save(destfile)
            # GET: /download/note.txt
            # return redirect(url_for('download_file', filename=filename))
            return redirect(url_for('upload_file'))            
            # return destfile
    
    filelist = listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', filelist=filelist)
        

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/view/<filename>')
def view_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

app.add_url_rule('/download/<filename>', 'download_file', build_only=True)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
