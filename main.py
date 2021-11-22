"""Smart garden"""
"""18.11.21"""
"""BORDON Clément"""


#modules import


import requests
from bs4 import BeautifulSoup
import RPi._GPIO as GPIO
import datetime
import time
from tzlocal import get_localzone
import os

#Local import
from mongo import Mongo_function as data_pesistence
from engine import Engine



class Weather_scrapper:

    def __init__(self):
        self.url = "https://www.meteoblue.com/fr/meteo/semaine/autruy-sur-juine_france_3035891"
        self.no_rain = {"precipitaion_value": " - ", "watering-time":os.environ.get("WATERDEB1")}
        self.little_rain = {"precipitaion_value": "0-2", "watering-time":os.environ.get("WATERDEB2")}
        self.medium_rain = {"precipitaion_value": "2-5", "watering-time":os.environ.get("WATERDEB3")}
        self.EGN = os.environ.get("EGN")
        self.value = None
        self.port = 4
        self.tz = get_localzone()
        
        

    def html_getter(self):
        source = requests.get(self.url)
        soup = BeautifulSoup(source.text, "html.parser")
        soup_filter1= soup.find_all("div", {"class": "tab_precip"})
        soup_filter2 = soup_filter1[4]
        self.value = None
        for i in soup_filter2:
            if self.no_rain.get("precipitaion_value") in i:
                self.value = self.no_rain.get("precipitaion_value")
            if self.little_rain.get("precipitaion_value") in i:
                self.value = self.little_rain.get("precipitaion_value")
            if self.medium_rain.get("precipitaion_value") in i:
                self.value = self.medium_rain.get("precipitaion_value")
        return self.value
    

    
    def watering(self, **kwargs):
        value = kwargs.get("precipitaion_value")
        watering_time = kwargs.get("watering-time")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.port, GPIO.OUT)
        time_now = datetime.datetime.now(self.tz)
        time_replace_microseconds = time_now.replace(microsecond=0)
        self.value["date_time"] = str(time_replace_microseconds)
        
        if value != None:
            
            GPIO.output(self.port, 1)
            print(f"--Watering--for--{watering_time}min")
            time.sleep(watering_time)
            GPIO.output(self.port, 0)
            GPIO.cleanup()
        return self.value



#Bot Engine

smartgarden_class = Weather_scrapper()
while smartgarden_class.EGN:
    run = Engine()
    run.check_time(smartgarden_class.watering(smartgarden_class.html_getter))
   

