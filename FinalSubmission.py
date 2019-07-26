import re
import cv2
import dlib
import time
import imutils
import keyboard
import threading
from mss import mss
from PIL import Image
from time import sleep
from google.cloud import vision

detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
cap = cv2.VideoCapture(0)

def multiple_people():
    '''
    Detects number of faces from the footage from camera using dlib's face
    landmark predictor
    '''
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    subjects = detect(gray, 0)
    numberOfPeople = len((subjects))
    #print(numberOfPeople)

    if numberOfPeople > 1:
        print("Multiple People Found, Cheating?")
    
    #time.sleep(20)

def screen_sharing():
    '''
    This function constantly checks for any screen sharing software,
    if the participant is using, through several parameters like some
    type of text on the screenshot using google cloud vision API
    '''
    client = vision.ImageAnnotatorClient() #GCP Cloud Vision API
    bbox = {'top': 0, 'left': 0, 'width': 1900, 'height': 1200}    
    
    sct = mss()
    #Grabbing real time screenshot of the device's screen
    sct_img = sct.grab(bbox)
    # cv2.imshow('screen', np.array(sct_img))
    image = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
    image.save('temp.png')
    
    with open('./temp.png', 'rb') as image_file:
        content = image_file.read()

    data = str(client.text_detection({'content': content}))
    output = re.search(r'((?<=Your desktop is currently shared with\s).*(?=\Stop Sharing))|((?<=nTeamViewer\s).*(?=\Session list))', str(data))
    
    if output:
        print("Maybe Cheating through Screen Sharing")
    
    #time.sleep(10)
        
def thread_scheduler():
    '''
    Thread for constant running the two functions 
    '''
    t_end = time.time() + 60
    keyboard.block_key('print screen')
    
    while time.time() < t_end:
        screen_sharing_thread = threading.Thread(target=screen_sharing)
        multiple_people_thread = threading.Thread(target=multiple_people)
        
        screen_sharing_thread.start()
        multiple_people_thread.start()
  
        screen_sharing_thread.join()
        multiple_people_thread.join()
    
    keyboard.unblock_key('print screen')

if __name__ == "__main__":
    thread_scheduler()
