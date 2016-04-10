#!/usr/bin/python

from datetime import datetime

class VibrateSensor(object):
    """Vibration Sensor"""

    def __init__(self):
        from sense_hat import SenseHat
        self.movement_threshold = 0.05
        self.sensor = SenseHat()
        self.current_reading = self.sensor.get_accelerometer_raw()
        self.last_reading = self.current_reading

    def read_sensor(self):
        """Set last_reading to prevous sensor reading, and read again"""
        self.last_reading = self.current_reading
        self.current_reading = self.sensor.get_accelerometer_raw()

    def motion_detected(self):
        """Returns True if there has been movement since the last read"""
        self.read_sensor()
        x_movement = abs(self.last_reading['x'] - self.current_reading['x'])
        y_movement = abs(self.last_reading['y'] - self.current_reading['y'])
        z_movement = abs(self.last_reading['z'] - self.current_reading['z'])
        if (x_movement > self.movement_threshold) \
                or (y_movement > self.movement_threshold) \
                or (z_movement > self.movement_threshold):
            return True
        else:
            return False

class Dryer(VibrateSensor):
    """Object for tracking the status of a dryer"""
    def __init__(self):
        super(Dryer, self).__init__()
        self.running = False
        self.refresh = False
        self.movement_started = datetime.now()
        self.movement_ended = datetime.now()

    def update(self):
        """Attempts to detect motion by running up to 5 polling events.
        A single motion event out of 5 will count as motion.
        Returns True when the status changed, or False if it remains the same"""
        changed = False
        for _ in range(5):
            if self.motion_detected():
                if not self.running:
                    running_time = datetime.now() - self.movement_started
                    if running_time.seconds > 60:
                        self.running = True
                        changed = True
                else:
                    self.movement_ended = datetime.now()
                return changed
        # We returned no motion 5 times in a row
        if self.running:
            stopped_time = datetime.now() - self.movement_ended
            if stopped_time.seconds > 60:
                self.movement_ended = datetime.now()
                self.running = False
                changed = True
        else:
            self.movement_started = datetime.now()
        return changed
