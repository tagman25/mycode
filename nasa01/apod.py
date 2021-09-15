#!/usr/bin/env python3
import requests
from pprint import pprint as pp
import webbrowser

## Define APOD 
apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=GGE0GWRhVZaidMhNRu8hazwzyDEV2q3AG6rNeOC6'    ## your key goes in place of DEMO_KEY

def main():
   ## Call the webservice
   apodread = requests.get(apodurl + mykey).json()

   ## display our Pythonic data
  # print("\n\nConverted Python data")
  # print(apodread)
  # input('\nThis is converted JSON. Press ENTER to continue.')

   pp(apodread)

   print(apodread['date'])
   print(apodread['explanation'])
   print('Link to the APOD:', apodread.get('hdurl','No HD URL for today!'))
   
   input('Press ENTER to view this phto of the day')
   webbrowser.open_new(apodread['hdurl'])

main()
