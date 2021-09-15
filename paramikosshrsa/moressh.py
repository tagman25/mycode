#!/usr/bin/python3
"""Learning about Python SSH | rzfeeser@alta3.com"""

# used to remove warnings from packages
import warnings

import paramiko
import json



# filter out any warnings with the word Paramiko
warnings.filterwarnings(action="ignore", module=".*paramiko.*")

def main():
    """Our runtime code that calls other functions"""
    with open('devices.json') as jsonfile:
        # describe the connection data
        credz = json.load(jsonfile)

    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    # loop across the collection credz
    with open('results.txt', 'w') as info:
        for cred in credz:
            ## create a session object
            sshsession = paramiko.SSHClient()

            ## add host key policy
            sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ## display our connections
            print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"), file=info)
            print('Connecting to... ' + cred.get('un') + '@' + cred.get('ip'))
            
            ## make a connection
            sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

            ## touch the file goodnews.everyone in each user's home directory
            sshsession.exec_command("touch /home/" + cred.get("un") + "/goodnews.everyone")

            ## list the contents of each home directory
            sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + cred.get("un"))

            ## display output
            print(sessout.read().decode('utf-8'), file=info)
            print('Added all results in file results.txt -> \'cat results.txt\' to read')
        
            ## close/cleanup SSH connection
            sshsession.close()

    print("Thanks for looping with Alta3!")

main()

