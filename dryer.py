#!/usr/bin/python

from pybrate import VibrateSensor
from datetime import datetime

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
