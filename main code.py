from Rpi import GPIO       #import GPIO Module
GPIO.setmode(GPIO.BOARD)   # Board Pin 
GPIO.setwarnings(False)    # set Warnings
GPIO.setup(40,GPIO.IN)     #declare input pin
GPIO.setup(5,GPIO.OUT)     #declare output pin
while True:                #use to While loop
  a=GPIO.input(40)         #input pin 
  if a==1:                 #condition
    GPIO.output(5,HIGH)    #Led On
  else:
    GPIO.output(5,LOW)     #Led Off
  
