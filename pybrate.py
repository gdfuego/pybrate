#!/usr/bin/python

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

