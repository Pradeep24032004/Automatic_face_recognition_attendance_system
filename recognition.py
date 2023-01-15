import cv2
import numpy as np
import face_recognition
imgSun = face_recognition.load_image_file('C:\\Users\\PRADEEP\\PycharmProjects\\pythonProject5\\bill gates.png')
imgSun = cv2.cvtColor(imgSun,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('C:\\Users\\PRADEEP\\PycharmProjects\\pythonProject5\\bill young.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
faceLock = face_recognition.face_locations(imgSun)[0]
encodeSun = face_recognition.face_encodings(imgSun)[0]
cv2.rectangle(imgSun, (faceLock[3], faceLock[0]),(faceLock[1], faceLock[2]),(255, 0, 255), 2)
faceLockTest = face_recognition.face_locations(imgTest)[0]
encodeSunTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLock[3], faceLock[0]),(faceLock[1], faceLock[2]),(255, 0, 255), 2)
results = face_recognition.compare_faces([encodeSun],encodeSunTest)
faceDis = face_recognition.face_distance([encodeSun],encodeSunTest)
print(results, faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.imshow('Sunder Pichai',imgSun)
cv2.imshow('Sunder Test',imgTest)
cv2.waitKey(0)