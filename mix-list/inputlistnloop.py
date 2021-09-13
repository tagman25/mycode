def main():
    network_list=[]
    with open('driverip.txt', 'r') as driverip:
        for sline in driverip:
            network_list.append(sline.rstrip('\n').split(' '))

    print(network_list)

    for driveandip in network_list:
      print('SSH to ' + driveandip[1] + ' using driver ' + driveandip[0])

main()
