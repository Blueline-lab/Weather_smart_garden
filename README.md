# Weather_smart_garden

Weather smart garden is a wattering bot.
It will checking the weather of the current day for watering your garden. 

If the rain was equal to an interval of X to Y < 5mm the bot will watering your garden during Z seconds. 
Configure Z values in the docker-compose.yml by modifying the env variables WATERDEB1, WATERDEB2, WATERDEB3.

The X to Y values equal to zero indicate no rain during the day and will active the watering by Z seconds define by WATERDEB1.
The X to Y values equal to 0-2 indiquate 0 to 2 millimeters of rain in the day and will active the watering by Z seconds define by WATERDEB2.
The X to Y values equal to 2-5 indiquate 2 to 5 millimeters of rain in the day and will active the watering by Z seconds define by WATERDEB2.

When a no rain or few rainy day is tiggered the engine module will process the watering at time define in the docker-compose.yml, define watering hour in the day by modifying the environnement variable HOUR.

# Electronic device
The main program will open GPIO PIN 4 and activate a relay. This relay will open a watervalve on the signal and close it after the delay define by WATERDEB1, WATERDEB2, WATERDEB3. This electronic network should protect by a resistance, without could occure dammage on the Raspberry.

# Versions
There is two version with data persistence and without data persistence: 

* After the main process in Version1 (branch main) the Mongodb function will save (on a Mongodb server define in the Mongodb module) the millimeter interval of    
  precipitation during the day, date & time, the watering duration. And the main program will clean GPIO pin and wait for the next check.

* After the main process in version1.1 (branch no_db) The main program will clean GPIO pin and wait for the next check.
