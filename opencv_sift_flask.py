from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


# run: export FLASK_APP=opencv_sift_flask.py; flask run
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
if __name__ == '__main__':
    app.run()
