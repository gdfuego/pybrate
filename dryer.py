#!/usr/bin/python

from pybrate import VibrateSensor
from datetime import datetime

class Dryer(VibrateSensor):
    """Object for tracking the status of a dryer"""
    def __init__(self):
        super(Dryer, self).__init__()
        self.running = False
        self.refresh = False
        self.movement_started = datetime(2000, 1, 1)
        self.movement_ended = datetime(2000, 1, 1)

    def update(self):
        """Update object states"""
        motion = self.motion_detected()
        if motion:
            if not self.running:
                running_time = datetime.now() - self.movement_started
                if running_time.seconds > 60:
                    self.running = True
            else:
                self.movement_ended = datetime.now()
        else:
            if self.running:
                stopped_time = datetime.now() - self.movement_ended
                if stopped_time.seconds > 60:
                    self.movement_ended = datetime.now()
                    self.running = False
            else:
                self.movement_started = datetime.now()
