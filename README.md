# Weather_smart_garden

Weather smart garden is a wattering bot who will check the weather of the current day, if the rain was X to Y mm the bot will watering your garden during Z seconds. Configure Z values in the docker-compose.yml.

The X to Y values equal to zero indicate no rain during the day and will active the watering by z seconds.
The X to Y values equal to 0-2 indiquate 0 to 2 millimeters of rain in the day and will active the watering by z seconds.
The X to Y values equal to 2-5 indiquate 2 to 5 millimeters of rain in the day and will active the watering by z seconds.

When a no rain or few rainy day is tiggered the engine file will process the watering at time define in the docker-compose.yml, define watering-time in the day by modifying the environnement variable HOUR.
