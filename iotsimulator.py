#!/usr/bin/python

'''
To generate <number> JSON data: 
$ ./iotsimulator.py <number>

'''

import sys
import datetime
import random
from random import randrange
import re
import copy


# Set number of simulated messages to generate
if len(sys.argv) > 1:
  num_msgs = int(sys.argv[1])
else:
  num_msgs = 1

# mapping of a guid and a apartment {guid: apartment}
device_apartment_map = {} 

# average annual temperature of each apartment
temp_base = {'Apartment1': 48.3, 'Apartment2': 55.3, 'Apartment29': 58.5, 'Apartment4': 43.1, 
		  'Apartment5': 51.8, 'Apartment17': 70.0, 'Apartment30': 70.7, 'Apartment42': 42.0, 
		  'Apartment6': 43.8, 'Apartment18': 52.7, 'Apartment31': 53.4, 'Apartment43': 64.8, 
		  'Apartment7': 66.4, 'Apartment19': 59.0, 'Apartment32': 40.4, 'Apartment44': 48.8, 
		  'Apartment8': 57.6, 'Apartment20': 45.4, 'Apartment33': 48.8, 'Apartment45': 59.4, 
		  'Apartment9': 49.9, 'Apartment21': 55.1, 'Apartment34': 45.1, 'Apartment46': 26.6, 
		  'Apartment10': 62.8, 'Apartment22': 60.4, 'Apartment35': 42.9, 'Apartment47': 51.8, 
		  'Apartment11': 63.5, 'Apartment23': 51.7, 'Apartment36': 47.8, 'Apartment48': 59.6, 
		  'Apartment12': 60.3, 'Apartment24': 44.4, 'Apartment37': 49.0, 'Apartment49': 41.0, 
		  'Apartment13': 54.2, 'Apartment25': 47.9, 'Apartment38': 50.7, 'Apartment50': 48.6, 
		  'Apartment14': 54.5, 'Apartment26': 41.2, 'Apartment39': 44.4, 'Apartment51': 50.1, 
		  'Apartment15': 54.3, 'Apartment27': 42.7, 'Apartment40': 63.4, 'Apartment52': 62.4, 
		  'Apartment16': 55.6, 'Apartment28': 48.4, 'Apartment41': 45.2}

# latest temperature measured by sensors {guid: temperature}
current_temp = {}

# Fixed values
guid_base = "0-ZZZ12345678-"
destination = "0-AAA12345678"
format = "urn:example:sensor:temp"

# Choice for random letter
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

iotmsg_header = """\
{ "guid": "%s", 
  "destination": "%s", 
  "apartment": "%s", """

iotmsg_eventTime = """\
  "eventTime": "%sZ", """

iotmsg_payload ="""\
  "payload": {"format": "%s", """

iotmsg_data ="""\
	 "data": { "temperature": %.1f  }   
	 }
}"""


##### Generate JSON output:
if __name__ == "__main__":
	for counter in range(0, num_msgs):
		rand_num = str(random.randrange(0, 9)) + str(random.randrange(0, 9))
		rand_letter = random.choice(letters)
		temp_init_weight = random.uniform(-5, 5)
		temp_delta = random.uniform(-1, 1)

		guid = guid_base + rand_num + rand_letter
		apartment = random.choice(temp_base.keys())

		if (not guid in device_apartment_map): # first entry
			device_apartment_map[guid] = apartment
			current_temp[guid] = temp_base[apartment] + temp_init_weight	
			
		elif (not device_apartment_map[guid] == apartment):		# The guid already exists but the randomly chosen apartment doesn't match
			apartment = device_apartment_map[guid]

		temperature = current_temp[guid] + temp_delta
		current_temp[guid] = temperature  # update current temperature	
		today = datetime.datetime.today()
		datestr = today.isoformat()

		print re.sub(r"[\s+]", "", iotmsg_header) % (guid, destination, apartment),
		print re.sub(r"[\s+]", "", iotmsg_eventTime) % (datestr),
		print re.sub(r"[\s+]", "", iotmsg_payload) % (format),
		print re.sub(r"[\s+]", "", iotmsg_data) % (temperature)
