#!/usr/bin/env python
# data.py - for python 2.7+
# Version 1.0
# MET project by Chih-Yu (Andy) Liu, Tracy Lu, and Felix Wong

#  Main python script for:
#       1) getting new workout data
#       2) retraining
#       3) pushing out new optimal routine to spark core

# Usage: 'python met.py [spark id] [access code]' at the command line
#-----------------------------------------------------------------------------#


## get new workout data
import sys
import subprocess
p = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
out, err = p.communicate()

print out
print sys.argv[0], sys.argv[1]


# curl "https://api.spark.io/v1/devices/51ff66065067545736270187/temp?access_token=be2f2d8cd0cbd6844f3ff7871b86624f7bf1c505"







## retraining using ALL data





## push out new routine to spark cloud


