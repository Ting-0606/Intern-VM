#!/usr/bin/python3
import RPi.GPIO as GPIO
from hx711 import HX711
import time

GPIO.cleanup()

Dout_L = 14
Sck_L = 4 
Dout_H = 3
Sck_H = 2
GPIO.setmode(GPIO.BCM)


GPIO.setup(4, GPIO.OUT)
GPIO.setup(14, GPIO.IN)
GPIO.setup(2, GPIO.OUT)``
GPIO.setup(3, GPIO.IN)

try:
    
    hx711 = HX711(
        dout_pin=Dout_L,
        pd_sck_pin=Sck_L,
        channel='A',
        gain=64
    )

    hx711_2 = HX711(
        dout_pin=3,
        pd_sck_pin=2,
        channel='A',
        gain=64
    )

    hx711.reset()  # Reset the HX711
    hx711_2.reset()  # Reset the HX711
    
    if not hx711.is_ready():
        print("error for 1")

    if not hx711_2.is_ready():
        print("error for 2")


    
    
    while True:

        reading = hx711._read()
        reading_2 = hx711_2._read()
        print(f"1:{reading}")
        print(f"2:{reading_2}")
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nScript stopped.")
    


