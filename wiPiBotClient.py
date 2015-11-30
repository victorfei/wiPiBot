# client side
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

pwm_out1=GPIO.PWM(12,50)
pwm_out2=GPIO.PWM(13,50)

def motor_control(direction):
  print direction

  if (direction == "fwd"):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    pwm_out1=GPIO.PWM(12,50)
    pwm_out2=GPIO.PWM(13,50)
    
    pwm_out1.start(6.5)
    pwm_out2.start(8.5)
    time.sleep(0.5)
    GPIO.cleanup()

  if (direction == "bwd"):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    pwm_out1=GPIO.PWM(12,50)
    pwm_out2=GPIO.PWM(13,50)
    
    pwm_out1.start(8.5)
    pwm_out2.start(6.5)
    time.sleep(0.5)
    GPIO.cleanup()
   
  if (direction == "left"):     
    GPIO.setmode(GPIO.BCM)     
    GPIO.setup(12, GPIO.OUT)    
    GPIO.setup(13, GPIO.OUT)    
    pwm_out1=GPIO.PWM(12,50)   
    pwm_out2=GPIO.PWM(13,50)

    pwm_out1.start(6.5)
    pwm_out2.start(6.5)
    time.sleep(0.5)
    GPIO.cleanup()

  if (direction == "right"):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    pwm_out1=GPIO.PWM(12,50)
    pwm_out2=GPIO.PWM(13,50)

    pwm_out1.start(8.5)
    pwm_out2.start(8.5)
    time.sleep(0.5)
    GPIO.cleanup()
