from flask import *
from sift import *
from pdb import set_trace
import cv2
import glob
import _pickle as pickle
import matplotlib.pyplot as plt

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
print('Running app...')


# run:
# export FLASK_APP=opencv_sift_flask.py;export FLASK_DEBUG=1; flask run
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # render form to search image
        return render_template('index.html')

        # get the upload image file
        # http://flask.pocoo.org/docs/0.12/quickstart/#file-uploads
        # request.form["image"]

        # call to search_image(image) function that return /path/to/image.jpg

        # render the result, consider using ajax.


        # Dữ liệu thử nghiệm: Wang database
        # (download tại: http://wang.ist.psu.edu/~jwang/test1.zip).
        # SV chia thủ công thành 2 tập: tập
        # ảnh truy vấn (query) và tập ảnh được truy vấn (database).
        # Bộ DL này có 10 nhóm, mỗi nhóm 100 ảnh vì vậy tập ảnh truy vấn tối
        # thiểu mỗi nhóm 1 ảnh.


@app.route('/index_image', methods=['GET'])
def index_images():
    images_success = index_images_with_sift()

    flash('Indexed ' + str(images_success) + ' images')

    return render_template('index_image_result.html')

@app.route('/search', methods=['GET'])
# @app.route('/search', methods=['POST'])
def search():
    image = cv2.imread('static/query/10.jpg')
    matching_image = search_image(image, 'indexed_images/', 0.7, 5)

    if len(matching_image) == 0:
        print('Can not find image match with query')
    else:
        print(matching_image)
        print('There are ' + str(len(matching_image)) + ' results')

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
