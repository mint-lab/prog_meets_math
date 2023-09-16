import cv2 as cv

# Load a face detector
face_detector = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# Prepare an image in gray scale
img = cv.imread('data/poster.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect faces
faces = face_detector.detectMultiScale(gray)

# Visualize results
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
cv.imshow('Face Detection using OpenCV', img)
cv.waitKey()
cv.destroyAllWindows()