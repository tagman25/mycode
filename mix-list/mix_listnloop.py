def main():
    #below isnlist s of lists containing the drivers needed to connect to 
    #the switch IP addresses
    network_list=[['ios', '10.0.2.1'],['ios','10.0.55.1'],['ios-xr', '10.0.3.1']]

    for driveandip in network_list:
        print ('SSH to ' + driveandip[1] + ' using driver ' + driveandip[0])

main()
