import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Trig = 21
Echo = 20
Buzzer = 16

GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)
GPIO.setup(Buzzer,GPIO.OUT)

PWM = GPIO.PWM(Buzzer,1)
PWM.start(0);



def distance():
    
    GPIO.output(Trig, True)
    time.sleep(0.01)
    GPIO.output(Trig,False)
    
    Start = time.time()
    Stop = time.time()
    
    while GPIO.input(Echo) == 0:
        Start = time.time()
        
    while GPIO.input(Echo) == 1:
        Stop = time.time()
          
    Elapsed = Stop - Start
    distance  = (Elapsed * 34300)/2
    
    if(distance<=50):
        print("Distance = ",distance)
        PWM.ChangeDutyCycle(100 - (distance * 2))
        time.sleep(0.6)
        
    else:
        print("There is nothing.")
        PWM.ChangeDutyCycle(0)
        time.sleep(1)

if __name__=='__main__':
    
    try:
        while True:
            distance()

    except KeyboardInterrupt:
        PWM.stop()
        GPIO.cleanup()
