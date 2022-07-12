import serial
import time
from tkinter import *
import pyrebase
# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial(port='COM5', baudrate=9800, timeout=1)
time.sleep(2)
top=Tk()
con1={ "apiKey": "AIzaSyBcIK4whIilaupv0dhjdEviHozWU-hst_8",
 "authDomain": "connecting-3b1d9.firebaseapp.com",
  "databaseURL": "https://connecting-3b1d9-default-rtdb.firebaseio.com",
  "projectId": "connecting-3b1d9",
  "storageBucket": "connecting-3b1d9.appspot.com",
  "messagingSenderId": "160669340478",
  "appId": "1:160669340478:web:265408e1dacc03aab9526f",
  "measurementId": "G-3RH105P129"}
firebase=pyrebase.initialize_app(con1)
db=firebase.database()
while(True):
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        a=string.split(" ") # convert the unicode string to an int
        data1={"TEMPERATURE":a[0]}
        data2={"MOISTURE":a[1]}
        data3 = {"WATER": a[2]}
        db.child("user").child("Temperature").set(data1)
        db.child("user").child("Moisture").set(data2)
        db.child("user").child("Water").set(data3)
        a1=db.child("user").child("Temperature").get()
        a2= db.child("user").child("Moisture").get()
        a3 = db.child("user").child("Water").get()
        q1=dict(a1.val())
        for i in q1.values():
            print("Temperature:{}".format(i))
            if(int(i)>120):
                ser.write(bytes('1'),'uft-8')
        q2=dict(a2.val())
        for i2 in q2.values():
             print("Moisture:{}".format(i2))
             if (int(i2) > 120):
                ser.write(bytes('1'), 'uft-8')
        q3 = dict(a3.val())
        for i2 in q3.values():
            print("Water:{}".format(i2))

ser.close()