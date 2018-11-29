import googlemaps 
from datetime import datetime 
import configparser 
import json 
import logging

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(filename='traveltime.log',level=logging.INFO,format=FORMAT)
logger = logging.getLogger('traveltimeligger')

config = configparser.ConfigParser() 

with open('config.json', 'r') as f:
    config = json.load(f) 

google_key = config['DEFAULT']['GOOGLE_KEY'] 
home_address = config['DEFAULT']['HOME_ADDRESS'] 
dest_address = config['DEFAULT']['DEST_ADDRESS'] 

gmaps = googlemaps.Client(key=google_key) 
now = datetime.now() 
directions_result = gmaps.directions(home_address,
                                     dest_address,
                                     mode="driving",
                                     avoid="ferries",
                                     departure_time=now
                                    ) 

#print(directions_result[0]['legs'][0]['distance']['text'])
logger.info(directions_result[0]['legs'][0]['duration']['text'])
#print(directions_result[0]['legs'][0]['duration']['text'])
