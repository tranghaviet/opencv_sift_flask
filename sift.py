import cv2
import glob
import _pickle as pickle
from pdb import set_trace
from operator import itemgetter

def index_images_with_sift(input_path='static/database/',
                           output_path='indexed_images/'):
    """
    Index images using sift
    :param str input_path:
    :param str output_path:
    """
    print('starting index...')
    # get all image_url in database
    images = glob.glob(input_path + '*.jpg')

    for image_path in images:
        image_name = image_path.split("/")[2].split(".")[0]
        img = cv2.imread(image_path)
        print('Index image ' + image_name)
        # Convert them to greyscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # sift extraction
        sift = cv2.xfeatures2d.SIFT_create()
        # sift.detect() finds the keypoint in the images
        keypoint, descriptor = sift.detectAndCompute(gray, None)

        # Store and Retrieve keypoint features
        file = output_path + image_name + ".txt"
        pickle.dump((descriptor, image_path), open(file, "wb"))

        # file = output_path + str(image_name) + '.txt'
        # db_des, db_img = pickle.load(open(file, "rb"))
        # print(descriptor == db_des)

    return len(images)


def search_image(image, distance_rate, number_match_min, db_images, k=2,
                 indexed_images_folder='indexed_images/'):
    """
    Search an image in database using sift
    :param image:
    :param float distance_rate:
    :param int number_match_min: so keypoint match nho nhat de lay anh
    :param int k:
    :param str indexed_images_folder:
    :return: list matching images
    """

    # fake:
    # image = cv2.imread('static/query/10.jpg')
    # indexed_images_folder, distance_rate, number_match_min, = ('indexed_images/', 0.7, 5)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    image_keypoint, image_descriptor = sift.detectAndCompute(gray, None)

    print("Start searching")
    bf = cv2.BFMatcher()
    results = []
    # image_numbers_database = []

    # for i in range(1, 1000):
    for image_path, db_descriptor in db_images.items():
        # file = indexed_images_folder + '/' + str(i) + '.txt'
        # db_descriptor = pickle.load(open(file, "rb"))[0]

        # so sanh cac keypoint cua anh tim kiem voi du lieu anh trong DB
        matches = bf.knnMatch(image_descriptor, db_descriptor, k)
        # FLANN_INDEX_KDTREE = 0
        # index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        # search_params = dict(checks=50)
        # flann = cv2.FlannBasedMatcher(index_params, search_params)
        # matches = flann.knnMatch(image_descriptor, db_descriptor, k=2)

        # set_trace()
        good = []
        for first, second in matches:
            if first.distance < distance_rate * second.distance:
                good.append([first])

        good_len = len(good)
        # matching_keypoints.append(good_len)
        # image_numbers_database.append(i)

        # if number of good keypoint greater than number_match_min, take it.
        if good_len > number_match_min:
            matching_image = {
                'image': image_path,
                'matching_kp': good_len
            }
            results.append(matching_image)

            # # draw matcher
            # img_in_db = cv2.imread(image_path, 0)
            # img_in_db_kp, img_in_db_des = sift.detectAndCompute(
            #     cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), None)

            # img_matcher = cv2.drawMatchesKnn(img_in_db, img_in_db_kp, image,
            #                                  image_keypoint, sorted(matches, key = lambda x:x.distance), None,
            #                                  # image_keypoint, good, None,
            #                                  flags=2)
            # cv2.imwrite('indexed_images/' + image_path[:16], img_matcher)

    results = sorted(results, key=itemgetter('matching_kp'), reverse=True)

    return results
