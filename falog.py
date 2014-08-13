#!/usr/bin/env python
# -*- coding: utf-8 -*-

_copyright = 'Farsheed Ashouri'
'''
   ___              _                   _ 
  / __\_ _ _ __ ___| |__   ___  ___  __| |
 / _\/ _` | '__/ __| '_ \ / _ \/ _ \/ _` |
/ / | (_| | |  \__ \ | | |  __/  __/ (_| |
\/   \__,_|_|  |___/_| |_|\___|\___|\__,_|

Just remember: Each comment is like an appology! 
Clean code is much better than Cleaner comments!

'''


import time
import sys
import os
from blessings import Terminal


term = Terminal()
LOGNAME = '.falog'


def now():
    '''Get current time in a fancy format'''
    localtime = time.localtime()
    result = time.strftime("%Y.%m.%d %H:%M:%S", localtime)
    return str(result)

def read():
    '''read user log'''
    data = ' '.join(sys.argv[1:])
    if data.strip():
        return data.strip()
    else:
        if os.path.isfile(LOGNAME):
            with open(LOGNAME, 'r') as log:
                for line in log.readlines():
                    l = line.split()
                    datepart = ' '.join(l[:2])
                    info = ' '.join(l[2:])
                    final = '{t.blue}{now}{t.normal}  {info}'.format(now=datepart,
                                info=info, t=term)
                    print final


def generate_log():
    '''generate the log based on two functions'''
    
    if read():
        log = '{now}  {read}\n'.format(now=now(), read=read())
        return log


def write():
    '''heck if fa.log file is available and write to it in append mode'''
    data = generate_log()
    if data:
        with open(LOGNAME, 'a') as log:
            log.write(data)



if __name__ == '__main__':
    write()
