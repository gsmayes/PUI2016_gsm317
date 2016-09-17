#Author: Gregory Mayes, NYU, September 2016
############################
#Code written to pull tracking information for each vehicle
#on a bus line from the MTA API interface for HW2 of PUI2016

from __future__ import print_function
import json
import urllib2
import sys

if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python show_bus_locations.py MTA_KEY BUS_LINE")
    sys.exit()

mtakey = sys.argv[1]
busline = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(mtakey, busline)

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
json.loads(data)

data.keys()
