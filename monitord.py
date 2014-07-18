#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import thread
import subprocess
import time
import os
import string

exitFlag = False

def run_shell(command, log, interval):
	args = string.split(command)
	while(True):
		if(exitFlag):
			thread.exit()
		print 'thread ' + command + ' ticks'
		logFile = open(log, 'a')
		subprocess.call(args, stdout=logFile, stderr=subprocess.STDOUT)
		time.sleep(interval)

print 'starting'
for command,log in config.commands:
	try:
		thread.start_new_thread(run_shell, (command, log, config.interval))
	except:
		print 'Something went wrong with ' + command
try:
	while(True):
		time.sleep(1)
except KeyboardInterrupt:
	print 'Finishing threads'
	exitFlag = True;
