import RPi.GPIO as GPIO
import time

GPIO.cleanup()
SW_0 = 17  # Forward M (switch)
SW_1 = 15  # Reverse M (switch)
IN1 = 27   # Forward M (motor control)
IN2 = 22   # Reverse M (motor control)

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

GPIO.setup(SW_0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        sw0_state = GPIO.input(SW_0)
        sw1_state = GPIO.input(SW_1)
        
        # Set IN1 HIGH if SW_0 is pressed (LOW), else LOW
        GPIO.output(IN1, GPIO.LOW if sw0_state else GPIO.HIGH)
        
        # Set IN2 HIGH if SW_1 is pressed (LOW), else LOW
        GPIO.output(IN2, GPIO.LOW if sw1_state else GPIO.HIGH)
        
        print(f"SW_0: {sw0_state} | SW_1: {sw1_state} | IN1: {GPIO.input(IN1)} | IN2: {GPIO.input(IN2)}")
        time.sleep(0.1)  # Reduced delay for more responsive control
        
except KeyboardInterrupt:
    GPIO.cleanup()