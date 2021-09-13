#! usr/bin/env python3

footballstats = [{"Name": "Jameis Winston","TD": 5,"Pass Yds": 148,"Team": "New Orleans Saints"}, {"Name": "Taysom Hill","TD": 0,"Pass Yds": 3,"Team": "New Orleans Saints"}]

for x in footballstats:
    if x['Name'] == "Jameis Winston":
      print(x['TD'])
    else:
      print("Not Jamies Winston")
