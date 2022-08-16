import cv2,os,urllib.request
import numpy as np
from django.conf import settings
face_detection_videocam = cv2.CascadeClassifier(os.path.join(
			settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))
face_detection_webcam = cv2.CascadeClassifier(os.path.join(
			settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))

class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.

		# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		# faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
		# for (x, y, w, h) in faces_detected:
		# 	cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
		# frame_flip = cv2.flip(image,1)
		ret, jpeg = cv2.imencode('.jpg',image)
		return jpeg.tobytes()


class IPWebCam(object):
	def __init__(self):
		# self.url = "http://192.168.0.100:8080/shot.jpg"
		self.url = "http://192.168.43.1:8080/shot.jpg"

		#My exp
		self.video = cv2.VideoCapture("http://192.168.43.1:8080/video")


	def __del__(self):
		# cv2.destroyAllWindows()
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		imgResp = urllib.request.urlopen(self.url)
		imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
		img= cv2.imdecode(imgNp,-1)
		# # We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# # so we must encode it into JPEG in order to correctly display the
		# # video stream
		# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		# faces_detected = face_detection_webcam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
		# for (x, y, w, h) in faces_detected:
		# 	cv2.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
		# resize = cv2.resize(img, (640, 480), interpolation = cv2.INTER_LINEAR)
		# frame_flip = cv2.flip(resize,1)
		ret, jpeg = cv2.imencode('.jpg',img)
		return jpeg.tobytes()
