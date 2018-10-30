#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import tm1637



# Initialize the clock (GND, VCC=3.3V, Example Pins are DIO-20 and CLK21)
Display = tm1637.TM1637(CLK=20, DIO=21, brightness=1.0)

try:
    print "Starting clock in the background (press CTRL + C to stop):"
    Display.StartClock(military_time=False)
    #print 'Continue Python script and tweak Display!'
    Display.SetBrightness(1.0)
    #Display.ShowDoublepoint(False)
    #sleep(5)
    #loops = 3
    while True:
        
        #for i in range(0, 10):
        Display.ShowDoublepoint(True)
        sleep(0.5)
        Display.ShowDoublepoint(False)
        sleep(0.5)
   
    Display.StopClock()

except KeyboardInterrupt:
    print "Properly closing the clock and open GPIO pins"
    Display.cleanup()

