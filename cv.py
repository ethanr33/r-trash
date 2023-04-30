import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="natural-engine-385300-20e8fcd6a069.json"
# Imports the Google Cloud client library
from google.cloud import vision
import cv2
import requests
import serial
import time
# Open the serial port at 9600 baud rate
ser = serial.Serial('/dev/tty.usbmodem1301', 9600)


url = 'http://34.125.240.67/api/Trash'

camera = cv2.VideoCapture(0)

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('')
while True:
    # Loads the image into memory
    ret, image = camera.read()
    success, encoded_image = cv2.imencode('.jpg', image)
    cv2.imwrite('hello.jpg',image)
    if ret:
        content2 = encoded_image.tobytes()

        image = vision.Image(content=content2)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        #print('Labels:')
       # print(response)
        # for label in labels:
        #     print(label.description)
        

        descriptions = [label.description for label in labels]
        for description in descriptions:
            if "bottle" in description or "can" in description or "soda" in description or "water" in description:
                requests.post(url, params={'type':'R'})
                print('Labels:')
                print(response)
                print("it works!\n")
                x = 50
                print("moving in\n")
                ser.write(str(x).encode())
                time.sleep(2)
                x = 90
                print("moving out\n")
                ser.write(str(x).encode())
                time.sleep(2)
                
                break
            elif "Plastic" in description or "snack" in description or "Electric blue" in description:
                requests.post(url, params={'type':'N'})
                print('Labels:')
                print(response)
                print("its garbo\n")
                x = 130
                print("moving in\n")
                ser.write(str(x).encode())
                time.sleep(2)
                x = 90
                print("moving out\n")
                ser.write(str(x).encode())
                time.sleep(2)
                
            else:
                requests.post(url, params={'type':'E'})

# Close the serial port
ser.close()