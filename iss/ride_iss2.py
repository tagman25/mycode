#! /usr/bin/env pthon3

import requests

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    helmetson = requests.get(MAJORTOM).json()

    ##display Python Data
    print('\n\nConverted Python data')
    print(helmetson)

    for x in helmetson['people']:
         print(f"{x['name']} is on {x['craft']}")
main()
