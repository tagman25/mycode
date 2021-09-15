#! /usr/bin/env python3

'''Tracking || Tracker ISS'''

import urllib.request
import json

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    ## Call the webservice (webpage)
    groundctrl = urllib.request.urlopen(MAJORTOM)
    
    ## put fileobject into helmet
    helmet = groundctrl.read()
    
    ##Decode helmet from JSON to Ptyhon data dictionary
    helmetson = json.loads(helmet.decode('utf-8'))

    ##Display Python Data
    print('\n\n Converted Python Data')
    print(helmetson)

    print('\n\nPeople in space: ', helmetson['number'])
    people = helmetson['people']
    print (people)

main()
