from flask import Flask, render_template, redirect, url_for, request, json
import pdb
from werkzeug import secure_filename
import os
app = Flask(__name__, static_url_path = "")
UPLOAD_FOLDER = './static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/")
def hello():
    return render_template('home.html', user_image = "/a.jpg")

@app.route("/upload_image", methods = ['POST'])
def upload_image():
    f = request.files['file']
    filename = secure_filename(f.filename)
    filepath= os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
    f.save(filepath)
    # pdb.set_trace()
    return json.dumps(
        {
            'status':'OK',
            'filePath':  "img/"+filename
        }
    )

@app.route('/get_images', methods = ['POST'])
def uploaded_file():
    return json.dumps(
        {
            'filePath': "img/Selection_002.png"
        }
    )

