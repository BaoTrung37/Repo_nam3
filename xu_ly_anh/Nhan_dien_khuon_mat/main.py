import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

while True:
	ret, frame = video_capture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces =face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        # cv2.putText(frame,'PERSON',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

	cv2.imshow('video',frame)
	if cv2.waitKey(1) & 0xFF == ord(' '):
		break
video_capture.release()
cv2.destroyAllWindows()
