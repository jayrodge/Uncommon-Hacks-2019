import cv2
import dlib
import time
import imutils
from time import sleep
from imutils import face_utils

detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
cap = cv2.VideoCapture(0)

def main_logic():
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    subjects = detect(gray, 0)
    numberOfPeople = len((subjects))
    print(numberOfPeople)

    if numberOfPeople > 1:
        print("Maybe Cheating")

def time_scheduler():
    t_end = time.time() + 5

    while time.time() < t_end:
        main_logic()

time_scheduler()