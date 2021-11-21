from tzlocal import get_localzone
import datetime
import time
import os

class Engine():
    def __init__(self):
        self.local_zone = get_localzone()
        self.watering_time = os.environ.get("HOUR")


    def check_time(self, function):
        dt_time = datetime.datetime.now(self.local_zone)
        dt_time_nomicrosecond = str(time.replace(microsecond=0))
        h_m = str(dt_time_nomicrosecond[11:13])
        if h_m == self.watering_time:
            function()
        

