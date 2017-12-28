import cv2

# Read an image
img = cv2.imread('./static/database/10.jpg')

# get gray of image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# SIFT extraction
sift = cv2.xfeatures2d.SIFT_create()

# detect ketpoints
kp = sift.detect(gray,None)

# draw new image with keypoints
img1 = cv2.drawKeypoints(gray, kp, img) # keypoint be smallen
cv2.imwrite('sift_keypoints.jpg', img1)

# keypoint with real size and orientation
# draw a circle with size of keypoint and it will even show its orientation
img2 = cv2.drawKeypoints(gray, kp, img, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite('sift_keypoints_flags.jpg', img2)

# detect and compute keypoint
keypoints, descriptors = sift.detectAndCompute(gray,None)
