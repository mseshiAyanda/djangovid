from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from streamapp.camera import VideoCamera, IPWebCam
from .models import Cam
from django.utils import timezone
# Create your views here.

def index(request):
	return render(request, 'streamapp/home.html')

def gen(camera,cam_type):
	webcam_frames=0
	ipcam_frames=0
	while True:
		if cam_type == 0:   #WebCam
			webcam_frames+=1
			if webcam_frames %100 ==0:
				temp_cam = Cam.objects.get(id=1)
				temp_cam.framecount+=webcam_frames
				temp_cam.timestamp = timezone.now()
				temp_cam.save()
				print("Webcam Updated")
		if cam_type == 1:  #IPCam
			ipcam_frames+=1
			if ipcam_frames %100 ==0:
				temp_cam = Cam.objects.get(id=2)
				temp_cam.framecount+=ipcam_frames
				temp_cam.timestamp = timezone.now()
				temp_cam.save()
				print("IPcam Updated")
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def webcam_feed(request):
		return StreamingHttpResponse(gen(IPWebCam(),0),
					content_type='multipart/x-mixed-replace; boundary=frame')
def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera(),1),
					content_type='multipart/x-mixed-replace; boundary=frame')
