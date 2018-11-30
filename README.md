# TavelTimeLogger

Python script that logs the travel time between two adddresses.  Originally created when needign to scout new potential work locations.  Use this script + cron to log the travel time over the course of normal commuting hours.

### Configuration

The folllowing configuration values are used:
* GOOGLE_KEY - Your Google Maps API Key
* START_ADDRESS - The starting address for the distance/directions api
* DESTINATION_ADDRESS - The destination address for the distance/directions api
* LOG_LOCATION - physical location and name of the log file
* LOG_FORMAT - the format of the log file

### Configuration Example
```
{
  "DEFAULT": {
    "GOOGLE_KEY": "put your key here",
    "START_ADDRESS": "1 Elm Street, Anywhere, USA",
    "DESTINATION_ADDRESS": "2 State Street, Noplace, USA",
    "LOG_LOCATION": "traveltime.log",
    "LOG_FORMAT": "%(asctime)-15s %(message)s"
  }
}
```

### instalation requirements

pip install googlemaps




