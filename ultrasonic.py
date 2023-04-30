import smtplib

SMTP_SERVER = 'smtp.gmail.com' 
SMTP_PORT = 587 
GMAIL_USERNAME = 'tsha813@gmail.com'
GMAIL_PASSWORD = '[Sensored for privacy reasons]'  
  

class Emailer:
    def sendmail(self, recipient, subject, content):

        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit

sender = Emailer()
sendTo = 'legocat813@gmail.com'
emailSubject = "Your trash is full"
emailContent = "Your trash is full, time to empty it!"


import requests
import time
url = 'http://34.125.240.67/api/Trash'

import serial
switch = True;
ser = serial.Serial('/dev/ttyACM0',9600)
#ser1 = serial.Serial('/dev/ttyACM1',9600)

val1 = 1
s = [0]
sensor11="" 
sensor22=""
sensor1 = 0
sensor2 = 0
count = 0
sent = False
while True:
    
    #response = requests.get(url).text
    #print(response)
    #if (response == "R"):
        #if recycle
     #   val1 = 50
        #ser1.write((str(val1)+ '\n').encode('utf-8'))
      #  time.sleep(5)
   # elif (response == "N"):
        #if garbage
     #   val1 = 130
        #ser1.write((str(val1)+ '\n').encode('utf-8'))
      #  time.sleep(5)
    
    #normal
   # val1 = 90
    #ser1.write((str(val1)+ '\n').encode('utf-8')) 
    s[0] = ser.readline().decode('utf-8')
    if switch:
        sensor11 = s[0][:2]
        switch = False
    else:
        sensor22 = s[0][:2]
        switch = True
    
    if sensor1 and not sensor1.isspace():
        sensor1 = int(sensor1)
    if sensor2 and not sensor22.isspace():
        sensor2 = int(sensor22)
   # sensor1 = int(sensor11)
   # sensor2 = int(sensor22)

    
    if(sensor11 < "30" or sensor22 < "30"):
        count = count + 1

    if(count > 4 and sent == False):
        sender.sendmail(sendTo, "Your trash can is full", "Your trash can is almost full, time to empty it.")
        sent = True
        count = 0
    sent = False
    
    #print ("sensor1: " + str(sensor1) + '\n')
    #print ("sensor2: " + str(sensor2) + '\n')
    print ("sensor1: " + sensor11 + '\n')
    print ("sensor2: " + sensor22 + '\n')
    #print(val1)


