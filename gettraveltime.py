import googlemaps 
from datetime import datetime 
import configparser 
import json 
import logging

config = configparser.ConfigParser() 
with open('config.json', 'r') as f:
    config = json.load(f) 

google_key = config['DEFAULT']['GOOGLE_KEY'] 
start_address = config['DEFAULT']['START_ADDRESS'] 
dest_address = config['DEFAULT']['DESTINATION_ADDRESS'] 
log_location = config['DEFAULT']['LOG_LOCATION'] 
log_format = config['DEFAULT']['LOG_FORMAT'] 

FORMAT = '%(asctime)-15s %(message)s'

logging.basicConfig(filename=log_location,level=logging.INFO,format=log_format)
logger = logging.getLogger('traveltimeligger')





gmaps = googlemaps.Client(key=google_key) 
now = datetime.now() 
directions_result = gmaps.directions(start_address,
                                     dest_address,
                                     mode="driving",
                                     avoid="ferries",
                                     departure_time=now
                                    ) 

#print(directions_result[0]['legs'][0]['distance']['text'])
logger.info(directions_result[0]['legs'][0]['duration']['text'])
#print(directions_result[0]['legs'][0]['duration']['text'])
