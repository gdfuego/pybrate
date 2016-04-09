#!/usr/bin/python

from sense_hat import SenseHat
from time import sleep, ctime

sense = SenseHat()

last = sense.get_accelerometer_raw()

while True:
        current = sense.get_accelerometer_raw()
    X = abs(last['x'] - current['x'])
    Y = abs(last['y'] - current['y'])
    Z = abs(last['z'] - current['z'])

    if (X > 0.05) or (Y > 0.05) or (Z > 0.05):
                print("%s - Moving" % ctime())

    last = current
    sleep(2)
