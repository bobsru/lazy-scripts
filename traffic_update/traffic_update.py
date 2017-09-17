#
# Author: Srujana Bobba
# traffic_update.py scipt: 
# 	Gets the driving time between 2 locations from google maps
# 	Notification is displayed on the mac with the link to go the maps
# 	Sends iMessage to a mobile number.

# Required packages: pync, googlemaps, sendMessage.applescript file

# Update below parameters with your own
GOOGLEMAPS_API_KEY = ''
TARGET_PHONE_NUMBER = ''
FROM_ADDRESS = 'Millennium Park, Chicago, IL 60601'
TO_ADDRESS = 'Willis Tower Skydeck, 233 S Wacker Dr, Chicago, IL 60606'
GOOGLE_MAPS_LINK = 'https://www.google.com/maps/dir/Millennium+Park,+Chicago,+IL/Willis+Tower+Skydeck,+South+Wacker+Drive,+Chicago,+IL/@41.8831931,-87.6326005,16z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x880e2ca70b00f081:0xcbf62372ee30a12b!2m2!1d-87.6193938!2d41.8827024!1m5!1m1!1s0x880e2cbf1d3c61a7:0xcee917a8ddbc62f1!2m2!1d-87.635915!2d41.8788761'

from datetime import datetime
import googlemaps
import json
gmaps = googlemaps.Client(key=GOOGLEMAPS_API_KEY)


# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions(FROM_ADDRESS,TO_ADDRESS,
                                     mode="driving",
                                     departure_time=now)

time_to_home =  directions_result[0]['legs'][0]['duration_in_traffic']['text']

# Display notification on your mac with a link to google maps with prepopulated TO and FROM fields. 
from pync import Notifier
import os

Notifier.notify(time_to_home,title='Traffic Update', open=GOOGLE_MAPS_LINK)
Notifier.remove(os.getpid())

Notifier.list(os.getpid())

# Send a text message
from subprocess import call
call(["osascript","sendMessage.applescript",TARGET_PHONE_NUMBER,
	"Hello, current time from Millennium park to Skydeck is: "+time_to_home])
