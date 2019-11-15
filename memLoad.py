# file: cpuLoad.py
#
# Simulate RAM load
#
# autor: Andrei Paplauski
# Contact: xpapla00@stud.fit.vutbr.cz
#


#!/usr/bin/env python3

import sys
import time


MB=1024*1024

SIZE=1*MB

sleepTime=0


def printHelp():
    print("Script simulate usage of given amount of RAM\n"
    "USAGE: \n"
    "memLoad.py MEMORYSIZE [SLEEP TIME]\n"
    "\tMEMORYSIZE - size of memory in MB to allocate\n"
    "\tSLEEP TIME - time to sleep in seconds, if you want program to exit on timer\n"
    )

def parseArgs(args:list):
    if(len(args) < 1):
        printHelp()
        sys.exit(-1)
    global SIZE
    SIZE = int(args[0]) * MB

    global sleepTime
    if(len(args) > 1 ):
        sleepTime=int(args[1])


def main(args:list):
    parseArgs(args)

    #set maximum size of string to 512 bytes
    stringSize=512
    global SIZE
    stringArray = []

    if(SIZE > stringSize):
        for i in range(SIZE // stringSize):
            stringArray.append(bytearray(stringSize))
            SIZE=SIZE - stringSize
        stringArray.append(bytearray(SIZE))

    if(sleepTime > 0):
        print("Sleep for {} seconds".format(sleepTime))
        time.sleep(sleepTime)
    else:
        input("Press ENTER to stop program...")


if __name__=="__main__":
    main(sys.argv[1:])
