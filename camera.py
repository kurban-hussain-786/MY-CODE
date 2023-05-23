import cv2 
\
from pygame import _camera_opencv
camera=cv2.VideoCapture(0)


while True:
   
   rat,image=camera.read()
   
   cv2.imshow('my first camera',image)
   if cv2.waitKey(1) & 0xff==ord('a'):
      break
   
camera.release()
cv2.destroyAllWindows()