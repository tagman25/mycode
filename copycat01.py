#! /usr/bin/env python3
import shutil
import os
# The following set the directory that this program is going to run from
os.chdir('/home/student/mycode')
# The following copies a file from source to destination (source,destination) with 'quotes' around file names
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')
# The following line will create the directory if it does not exist already
shutil.copytree('5g_research/', '5g_research_backup')
