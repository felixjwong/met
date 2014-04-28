#!/usr/bin/env python
# data.py - for python 2.7+
# Version 1.0
# MET project by Chih-Yu (Andy) Liu, Tracy Lu, and Felix Wong

#  Main python script for:
#       1) getting new workout data
#       2) retraining
#       3) pushing out new optimal routine to spark core

# Usage: 'python met.py [spark id] [access code] [objective AR]' at the command line
# Sample Usage: 'python met.py 51ff66065067545736270187 be2f2d8cd0cbd6844f3ff7871b86624f7bf1c505 10 1500'
#-----------------------------------------------------------------------------#

# packages
import sys
import subprocess
import os, os.path
import filecmp

# minimal number of training datasets we need
trainingthreshold = 5

#--------------------------DATA IMPORT MODULE--------------------------------#
# get new workout data via
# curl "https://api.spark.io/v1/devices/51ff66065067545736270187/temp?access_token=be2f2d8cd0cbd6844f3ff7871b86624f7bf1c505"
#   > data/sparkid/1.txt

directory = './data/'+sys.argv[1]+'/'
alldatafiles = [item for item in os.listdir(directory) if '.txt' in item]
i = len(alldatafiles)+1

p = subprocess.Popen(['curl', "'https://api.spark.io/v1/devices/"+sys.argv[1]+"/temp?access_token="+sys.argv[2]+"'", ">", sys.argv[1]+"/"+str(i)+".txt"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out, err = p.communicate()
#print out


#--------------------------DATA CURATION MODULE--------------------------------#
# eliminate redundant data
directory = './data/'+sys.argv[1]+'/'
alldatafiles = [item for item in os.listdir(directory) if '.txt' in item]
#print alldatafiles

removefiles = []
for item in alldatafiles:
    for item1 in alldatafiles:
            if item != item1:
                if filecmp.cmp(directory+item,directory+item1):
                    if (item not in removefiles) and (item1 not in removefiles):
                        removefiles.append(item1)
for item in removefiles:
    os.remove(directory+item)

#--------------------------RETRAINING MODULE--------------------------------#

# call processing.py with all needed cmd line arguments
p = subprocess.Popen(['python', 'processing.py', sys.argv[1], sys.argv[3]], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out, err = p.communicate()
#print out


#------------------GETTING DATA TO SPARK CORE MODULE-----------------------------#
# sparkid/optimal.txt

## push out new routine to spark cloud
# put optimal.txt onto spark cloud

"""
    
    COMPLEMENTARY API CALL
    POST /v1/devices/{DEVICE_ID}/{FUNCTION}
    
    # EXAMPLE REQUEST
    curl 0123456789abcdef01234567/brew \
    -d access_token=1234123412341234123412341234123412341234 \
    -d "args=coffee"
    
    
"""

if i >= trainingthreshold:
    fopen = open(directory+'optimal.tsv');
    optimalroutine = []
    for line in fopen.readlines():
        currentline = line.split(' ',)
        optimalroutine.append([eval(item) for item in currentline])
    fopen.close()

    for item in optimalroutine:
        argin = str(item[0])+','+str(item[1])+','+str(item[2])+','+str(item[3])
        #print 'curl', "'https://api.spark.io/v1/devices/"+sys.argv[1]+"/metkey", "-d", "access_token="+sys.argv[2], "-d", "'"+argin+"'"
        p = subprocess.Popen(['curl', "'https://api.spark.io/v1/devices/"+sys.argv[1]+"/metkey", "-d", "access_token="+sys.argv[2], "-d", "'"+argin+"'"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out, err = p.communicate()



