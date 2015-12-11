# client side
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
pwm_out1=GPIO.PWM(12,50)
pwm_out2=GPIO.PWM(13,50)

motor_a = 8.0
motor_b = 7.0

print motor_a, motor_b

def speed_control(speed):
  global motor_a
  global motor_b

  if (speed == "up" and motor_a < 8.5 and motor_b > 6.5):
    motor_a = motor_a + 0.1
    motor_b = motor_b - 0.1

  if (speed == "down" and motor_a >7.5 and motor_b < 7.5):
    motor_a = motor_a - 0.1
    motor_b = motor_b + 0.1
  
  print motor_a, motor_b

def motor_control(direction):
  print direction
  
  global motor_a
  global motor_b
  global pwm_out1
  global pwm_out2
 
  if (direction == "fwd"):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    pwm_out1=GPIO.PWM(12,50)
    pwm_out2=GPIO.PWM(13,50)
    pwm_out1.start(motor_a)
    pwm_out2.start(motor_b)
    print motor_a, motor_b

 
  if (direction == "bwd"):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    pwm_out1=GPIO.PWM(12,50)
    pwm_out2=GPIO.PWM(13,50) 
    pwm_out1.start(motor_b)
    pwm_out2.start(motor_a)
   
  if (direction == "left"):     
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    pwm_out1=GPIO.PWM(12,50)
    pwm_out2=GPIO.PWM(13,50) 
    pwm_out1.start(motor_b)
    pwm_out2.start(motor_b)
   
  if (direction == "right"):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    pwm_out1=GPIO.PWM(12,50)
    pwm_out2=GPIO.PWM(13,50) 
    pwm_out1.start(motor_a)
    pwm_out2.start(motor_a)
   
  if (direction == "stop"):
    pwm_out1.stop()
    pwm_out2.stop()
    GPIO.cleanup()

def blink():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(21, GPIO.OUT)
  
  for i in range(4):
    GPIO.output(21, True)
    time.sleep(0.3)
    GPIO.output(21, False)
    time.sleep(0.3)
  
  
