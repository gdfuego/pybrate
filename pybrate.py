#!/usr/bin/python

from sense_hat import SenseHat
from time import sleep, ctime

SENSOR = SenseHat()

LAST = SENSOR.get_accelerometer_raw()

while True:
    CURRENT = SENSOR.get_accelerometer_raw()
    X = abs(LAST['x'] - CURRENT['x'])
    Y = abs(LAST['y'] - CURRENT['y'])
    Z = abs(LAST['z'] - CURRENT['z'])

    if (X > 0.05) or (Y > 0.05) or (Z > 0.05):
        print "%s - Moving" % ctime()

    LAST = CURRENT
    sleep(2)
