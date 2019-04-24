#!/usr/bin/env python3

import queue
import platform
import subprocess
import csv
import threading
import time

##################################
# Queues for threading
queueOutpuut = queue.Queue()
queueError = queue.Queue()
threadQueue = queue.Queue()
outlock = threading.Lock()
##################################

def ping(hostname,ip):
    # Option for the number of packets as a function of
    if platform.system().lower() == 'windows':
        param = '-n'
    else:
        param = '-c'
    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', ip]
    queueOutpuut.put([subprocess.call(command) == 0, hostname, ip])



def threadWrapperPing(ipList):
    # Holds all the threads that will be created
    threads = []

    ## getting ready for threads
    rows = []
    with open(ipList, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)

    for line in rows:
        # Limits threads to threadNumber, if you go over with queue size, it will sleep for 10 seconds then check again.
        while threadQueue.qsize() > 50: #thread limiter loop
            #Sleeps
            time.sleep(3)
        # Target is your function to run in parrel, and args are the arguments for the function
        t = threading.Thread( target=ping,args=(line[0],line[1]) )
        t.start()
        threads.append(t)

    # Rejoin the threads
    for t in threads:
        t.join()

    # Empty queue into whatever, probably a file
    finalList =[]
    while not queueOutpuut.empty():
        # Print function replace in not a template
        x = queueOutpuut.get()
        finalList.append(x)
    return finalList
