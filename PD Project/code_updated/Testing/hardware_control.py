# hardware_control.py
import RPi.GPIO as GPIO
import time

class HardwareController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        # Define your GPIO pins (modify these according to your setup)
        self.led_pin = 10
        
        # Motor control pins
        self.motor_in1 = 27  # Motor control pin 1
        self.motor_in2 = 22  # Motor control pin 2
        
        # Switch input pins
        self.switch_sw0 = 17  # Switch 0 input
        self.switch_sw1 = 15  # Switch 1 input
        
        # Setup GPIO pins
        GPIO.setup(self.led_pin, GPIO.OUT)
        
        # Motor control pins as outputs
        GPIO.setup(self.motor_in1, GPIO.OUT)
        GPIO.setup(self.motor_in2, GPIO.OUT)
        
        # Switch pins as inputs with pull-up resistors
        GPIO.setup(self.switch_sw0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.switch_sw1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        # Add event detection for switches
        GPIO.add_event_detect(self.switch_sw0, GPIO.BOTH, callback=self.switch_changed, bouncetime=200)
        GPIO.add_event_detect(self.switch_sw1, GPIO.BOTH, callback=self.switch_changed, bouncetime=200)
        
        # Initial states
        self.led_state = False
        self.motor_state = "STOP"
        
        # Initialize motor to stopped state
        self.motor_stop()
        
    def switch_changed(self, channel):
        """Callback when either switch changes state"""
        self.update_motor_from_switches()
        
    def update_motor_from_switches(self):
        """Update motor based on switch states"""
        sw0_state = GPIO.input(self.switch_sw0)
        sw1_state = GPIO.input(self.switch_sw1)
        
        # At rest: both switches HIGH → motor STOP
        if sw0_state == GPIO.HIGH and sw1_state == GPIO.HIGH:
            self.motor_stop()
            self.motor_state = "STOP"
        
        # SW0 pressed (LOW), SW1 HIGH → IN1 LOW, IN2 HIGH (Motor DOWN)
        elif sw0_state == GPIO.LOW and sw1_state == GPIO.HIGH:
            GPIO.output(self.motor_in1, GPIO.LOW)
            GPIO.output(self.motor_in2, GPIO.HIGH)
            self.motor_state = "DOWN"
        
        # SW1 pressed (LOW), SW0 HIGH → IN1 HIGH, IN2 LOW (Motor UP)
        elif sw0_state == GPIO.HIGH and sw1_state == GPIO.LOW:
            GPIO.output(self.motor_in1, GPIO.HIGH)
            GPIO.output(self.motor_in2, GPIO.LOW)
            self.motor_state = "UP"
        
        # Both switches LOW → motor STOP (safety)
        else:
            self.motor_stop()
            self.motor_state = "STOP (SAFETY)"
    
    def led_on(self):
        GPIO.output(self.led_pin, GPIO.HIGH)
        self.led_state = True
        return "LED ON"
    
    def led_off(self):
        GPIO.output(self.led_pin, GPIO.LOW)
        self.led_state = False
        return "LED OFF"
    
    
    def get_motor_status(self):
        return self.motor_state
    
    def cleanup(self):
        GPIO.remove_event_detect(self.switch_sw0)
        GPIO.remove_event_detect(self.switch_sw1)
        GPIO.cleanup()