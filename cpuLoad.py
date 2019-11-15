# file: cpuLoad.py
#
# Simulate CPU load
#
# autor: Andrei Paplauski
# Contact: xpapla00@stud.fit.vutbr.cz
#


#!/usr/bin/env python3


import sys
import time

from multiprocessing import Process
from multiprocessing import cpu_count

sleepTime=0

def printHelp():
    print("Script simulate 100% usage of all cores of CPU\n"
    "USAGE: \n"
    "cpuLoad.py TIME\n"
    "\tTIME - amount of seconds to sleep(if you want script to stop on input, not on timer, pass negative value or zero)"
    )


def load():
    while True:
        42*42


def parseArgs(args:list):
    if(len(args) < 1):
        printHelp()
        sys.exit(-1)
    global sleepTime
    sleepTime=int(args[0])


def main(args:list):
    parseArgs(args)
    cpus = cpu_count()
    processes = []
    for i in range(cpus):
        p = Process(target=load)
        p.start()
        processes.append(p)

    if(sleepTime > 0):
        print("Sleep for {} seconds".format(sleepTime))
        time.sleep(sleepTime)
    else:
        input("Press ENTER to stop program...")

    for p in processes:
        p.terminate()


if __name__=="__main__":
    main(sys.argv[1:])
