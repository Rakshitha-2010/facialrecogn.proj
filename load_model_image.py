import numpy as np
import cv2
import os

import faceRecognition as fr 
print(fr)

test_img=cv2.imread(r'C:\Users\Rakshi\Desktop\FaceRecogn\testImg.jpg')

faces_detected,gray_img=fr.faceDetection(test_img)
print("Face Detected: ",faces_detected)

#Training will begin from here

face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(r'C:\Users\Rakshi\Desktop\FaceRecogn\trainingData.yml')

name={0:'Harish'}
for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)
    print("Confidence :",confidence)
    print("Label :",label)
    fr.draw_rect(test_img,face)
    predict_name=name[label]
    if(confidence<49):
        fr.put_text(test_img,'unknown',x,y)
        continue;
    fr.put_text(test_img,predict_name,x,y)

resized_img=cv2.resize(test_img,(1000,700))
cv2.imshow("Face Detection",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()