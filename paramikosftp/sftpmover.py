#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os
import getpass

device = input('What is the IP of the device you want to connect to? ')
uname = input ('what is your username?')
password = getpass.getpass()
## where to connect to
t = paramiko.Transport(device, 22) ## IP and port

## how to connect (see other labs on using id_rsa private/public keypairs)
t.connect(username=uname, password=password)

## Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
def movethemfiles(y):
    try:
        for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
          if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
             y.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location
    except:
        print('There was an error')
try:
    movethemfiles(sftp)
except:
    print('There wasn an error')
## close the connection
sftp.close() # close the connection

