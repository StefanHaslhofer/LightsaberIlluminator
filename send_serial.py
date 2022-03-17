# This python script listens to events of EmptyEpsilon´s local http server
# it creates light effects with connected leds and sounds an alarm with a connected bluetooth device
from time import sleep

import requests
import serial

arduino = serial.Serial('COM5', 9600)


def write_to_serial(x):
    if not arduino.is_open:
        arduino.open()
    print('writing to serial...')
    arduino.write(x.encode())