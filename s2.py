import time, datetime, sys
import RPi.GPIO as GPIO

sense pin = 7


GPIO.setmode(GPIO.BOARD)


last_time = time. time()
this_time = time.time()

RPM = 0
 #FUNCTION 'add event detect' RUNS AT INPUT CHANGE
def EventsPerTime (channel) :
  global RPM, this_time, last_time
  this_time = time.time()
  RPM = (1/(this_time - last_time))*60
  print('Current RPM =' ,' {:7.1f} ' . format (RPM)) #Instantaneous RPMs (not avg)
  last_time = this_time
GPIO. add_event_detect (sense_pin, GPIO.RISING, callback=EventsPerTime, bouncetime=1)
timedate = datetime.datetime.now().strftime ('%H : %M %Y%m%d %a' )
print ('System Active @ ',timedate)
print ('Ctrl C to quit')
try:
  for x in range (0, 1200) :
    time.sleep(0.5)
except:
   time sleep(2)
  GPIO.remove_event_detect (sense_pin)
  GPIO.cleanup()
  print ('Done')
