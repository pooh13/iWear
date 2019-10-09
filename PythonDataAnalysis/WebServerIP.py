import os
import requests
import serial

# IPAddress = requests.get("140.131.114.149:3389")

# print(IPAddress)

ser = serial.Serial("140.131.114.149", 3389, timeout=0.5)
print(serial.request)



