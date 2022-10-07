# How to limit threading in Python by using simple approach

import threading
import time

MAX_THREAD_COUNT = 30

def sampleThreadProgram():
    time.sleep(1)

def main():
	for x in range(1000):
		print('x is ' + str(x))
		while len(threading.enumerate())>=MAX_THREAD_COUNT:
			print('running threads are' + str(len(threading.enumerate())))
			time.sleep(1)
		t1 = threading.Thread(target=sampleThreadProgram, args=())
		t1.start()

main()