from sense_hat import SenseHat
import time
import random

 
sense = SenseHat()

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
sense.show_letter("1",text_colour=[r, g, b])
time.sleep(1)

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
sense.show_letter("2",text_colour=[r, g, b])
time.sleep(1)
 
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
sense.show_letter("3",text_colour=[r, g, b])
time.sleep(1)

 
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
sense.show_letter("4",text_colour=[r, g, b])
time.sleep(1)



sense.show_letter("!", text_colour=[0, 0, 0], back_colour=[255, 255, 255] )
time.sleep(1)
while True:
    sense.show_letter("1")
    time.sleep(1)
    sense.show_letter("2")
    time.sleep(1)
    sense.show_letter("3")
    time.sleep(1)
    sense.show_letter("4")
    time.sleep(1)
 
