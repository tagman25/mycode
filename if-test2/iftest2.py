#! /usr/bin/env python3
import ipaddress
import sys

ipchk = input('Apply an IP address: ')

if ipchk == '192.168.70.1': # is a match on that IP address
    print(f'Looks like the IP address of teh gateway was set: {ipchk}  This is not recommended')
elif ipchk:
    print(f'Looks like the IP address was set: {ipchk}')
else:
    print('You didn\'t add an IP address')

try:
    ipchk = ipaddress.ip_address(sys.argv[1])
    print('%s is a correct IP%s address.' % (ip, ip.version))
except ValueError:
    print('address/netmask is invalid: %s' % sys.argv[1])
except:
    print('Usage : %s  ip' % sys.argv[0])
