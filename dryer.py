#!/usr/bin/python

from pybrate import VibrateSensor
from datetime import datetime

class Dryer(VibrateSensor):
    def __init__(self):
        from datetime import datetime
        super(Dryer, self).__init__()
        self.running = False
        self.refresh = False
        self.movement_started = datetime(2000, 1, 1)
        self.movement_ended = datetime(2000, 1, 1)

    def update(self):
        motion = self.motion_detected()
        if motion:
            runningtime = datetime.now() - self.movement_started
            if (not self.running and runningtime > 60):
                self.running = True
