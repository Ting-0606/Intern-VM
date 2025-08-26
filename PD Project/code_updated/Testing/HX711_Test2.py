#!/usr/bin/python3
import RPi.GPIO as GPIO
from hx711 import HX711
import time

#GPIO.cleanup()


GPIO.setmode(GPIO.BCM)
print("initializing...")

try:
    #HX711_L
    hx711 = HX711(
        dout_pin=6,
        pd_sck_pin=5,
        channel='A',
        gain=64
    )
    #HX711_H
    hx711_2 = HX711(
        dout_pin=24,
        pd_sck_pin=23,
        channel='A',
        gain=64
    )

    hx711.reset()  # Reset the HX711
    hx711_2.reset()  # Reset the HX711
    
    while True:

        reading = hx711._read()
        reading_2 = hx711_2._read()
        print(f"L:{reading}")
        print(f"H:{reading_2}")
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nScript stopped.")
except Exception as e:
    print(f'Error:{e}')
finally:
    print('end')

