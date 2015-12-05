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

  if (direction == "fwd"):
    
    pwm_out1.start(motor_a)
    pwm_out2.start(motor_b)

  if (direction == "bwd"):
    
    pwm_out1.start(motor_a)
    pwm_out2.start(motor_b)
   
  if (direction == "left"):     

    pwm_out1.start(motor_a)
    pwm_out2.start(motor_b)
   

  if (direction == "right"):

    pwm_out1.start(motor_a)
    pwm_out2.start(motor_b)
   

  if (direction == "stop"):
    pwm_out1.stop()
    pwm_out2.stop()
  
  if (direction == "exit"):
    GPIO.cleanup()

def LED_control(power):
  print power
  if (power == "off"):
    GPIO.output(21, False)
     
  if (power == "on"):
    GPIO.output(21, True)
   
  if (power == "exit"):
    GPIO.cleanup()
    
