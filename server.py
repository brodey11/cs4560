#!/usr/bin/env python

from bluetooth import*
import os
import glob
import RPi.GPIO as GPIO
from time import sleep
import time


# def LED_ON():
#     GPIO.setwarnings(False)
#     GPIO.setmode(GPIO.BOARD)
#     GPIO.setup(40, GPIO.OUT, initial=0)
#     GPIO.output(40, GPIO.HIGH)

# def LED_OFF():
#     GPIO.output(40, GPIO.LOW)
    

GPIO.setmode(GPIO.BCM)

# init list with pin numbers
pinList = [26, 19, 13, 6, 12, 16, 20, 21]

# loop through pins and set mode and state to 'low'
for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop
SleepTimeL = 1



#while(1):



os.system("hciconfig hci0 piscan")

hostMACAddress = '00:1f:e1:dd:08:3d' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
server_socket = BluetoothSocket(RFCOMM)
server_socket.bind(("",PORT_ANY))

#light = LED()

#listens for data to be sent to the socket
server_socket.listen(1)
port = server_socket.getsockname()[1]


#identical UUID for connection to client

uuid = "a1bb5f8d-406d-4119-9cc8-f6c8395514ae"
"""
uuid = "2F234454-CF6D-4A0F-ADF2-F4911BA9FFA6"
"""
#port = bluetooth.PORT_ANY #arbitrary choice. However, it must match the port used by the client.
size = 1024






"""

advertise_service(server_socket, "Our Server", service_id = uuid,
                            service_classes = [uuid, SERIAL_PORT_CLASS],
                            profiles = [SERIAL_PORT_PROFILE])

#"""

client_socket = None



#print("here n")

client_socket, address = server_socket.accept()

#print ("here1")
if client_socket == None:
    print ("No client")

print ("Connection established with: " , address)

while(1):
    data = client_socket.recv(size).encode()    
    try: 
       client_socket.getpeername()
       still_connected = True
    except:
        still_connected = False
        print("DISCONNECTED\n")
    print ("recieved[%s] \n" % data)

    if data == "1"::
        #print("recieved 1\n")
        #LED_ON()
        GPIO.output(26, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        time.sleep(SleepTimeL);
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)
    elif data == "0":
        #print("recieved 0\n")
        #LED_OFF()
        GPIO.output(19, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        time.sleep(SleepTimeL)
        GPIO.output(19, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH)
    else:
        print("nothin\n")


client_socket.close()
server_socket.close()


"""
if __name__ == '__main__':
    main()
"""



