#!/usr/bin/env python

import time
import sys
import os

def now():
    '''Get current time in a fancy format'''
    localtime = time.localtime()
    result = time.strftime("%Y.%m.%d %M:%S", localtime)
    return str(result)

def read():
    '''read user log'''
    data = ' '.join(sys.argv[1:])
    if data.strip():
        return data.strip()
    else:
        if os.path.isfile('fa.log'):
            with open('fa.log', 'r') as log:
                print log.read()


def generate_log():
    '''generate the log based on two functions'''
    
    if read():
        log = '{now}  {read}\n'.format(now=now(), read=read())
        return log


def write():
    '''heck if fa.log file is available and write to it in append mode'''
    data = generate_log()
    if data:
        with open('fa.log', 'a') as log:
            log.write(data)



if __name__ == '__main__':
    write()
