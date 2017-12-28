from flask import Flask, render_template, redirect, url_for, request, json
from pdb import set_trace
from werkzeug import secure_filename
import os
from sift import *

app = Flask(__name__, static_url_path="")
UPLOAD_FOLDER = './static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def hello():
    return render_template('home.html', user_image="/a.jpg")


@app.route("/upload_image", methods=['POST'])
def upload_image():
    f = request.files['file']
    filename = secure_filename(f.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'],
                            secure_filename(f.filename))
    f.save(filepath)

    # pdb.set_trace()
    return json.dumps(
        {
            'status': 'OK',
            'filePath': "img/" + filename
        }
    )


@app.route('/get_images', methods=['POST'])
def uploaded_file():
    image = request.form['path']
    
    if not image:
        image = '/wall_paper.jpg'

    # set_trace()
    image = cv2.imread('static/' + image)

    matching_images = search_image(image, 0.7, 5)

    print(matching_images)

    # set_trace()
    if len(matching_images) == 0:
        return json.dump(
            {
                ''
            }
        )

    # set_trace()
    return json.dumps(
        {
            'filePath': 'database/' + str(matching_images[0]['image']) + '.jpg'
        }
    )

@app.route('/index_image', methods=['GET'])
def index_images():
    images_success = index_images_with_sift()

    flash('Indexed ' + str(images_success) + ' images')

    return render_template('index_image_result.html')
