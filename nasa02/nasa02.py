#! /usr/bin/env python3

import requests
import json

## Define NEOapi
neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = 'start_date=2018-06-01'
enddate = 'end_date=2018-06-08'
mykey = 'api_key=GGE0GWRhVZaidMhNRu8hazwzyDEV2q3AG6rNeOC6'

def get_data(url,key,start,end):
    if start != '':
        if end != '':
          data = requests.get(url+mykey+ '&' + start + '&' + end).json()
        else:
          data = requests.get(url+mykey+ '&' + start).json()
    else:
        data = requests.get(url+mykey).json()
    return data

def just_missed():
    miss_data = get_data(neourl,mykey,'','')
    for date in miss_data['near_earth_objects']:
        for date_value in miss_data['near_earth_objects'][date]:
           print(f"\nOn {date}, {date_value['name']} missed earth by: {date_value['close_approach_data'][0]['miss_distance']['lunar']} moon lengths.")

def main():
    #results = get_data(neourl,mykey,startdate,enddate)
    #print(results)
    just_missed()

main()
