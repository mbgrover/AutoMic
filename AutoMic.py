from flask import Flask, redirect, url_for, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import pdftotext

#Creates the Flask app (Secret Key is temporary, change after further development)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sinanbeskok'
app.config['UPLOAD_FOLDER'] = 'static/files'

#Creates the upload file input
class UploadFileForm(FlaskForm):
    file = FileField('File', validators=[InputRequired()]) #Checks if user has uploaded a file
    submit = SubmitField('Upload File') #Upload button!

@app.route('/', methods=['GET','POST'])

#Creating the main page
@app.route('/home', methods=['GET','POST'])
def home():
    form = UploadFileForm()

    #Saving the file uploaded by the user
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return redirect(url_for('script', scp = file.filename, cl=request.form['cl']))

    return render_template('index.html', form=form)

@app.route('/<scp>/<cl>', methods=['GET','POST'])
def script(scp,cl):
    charList = cl.split(',')
    fileName = scp
    micList = pdftotext.doTheThing(fileName, charList)
    return render_template('result.html', scp=scp, cl=micList)

if __name__ == '__main__':
    app.run(debug=True)