import sys
import time
n = 1
while True:
	if n % 10 == 0:
		print('Accident Detected')
	else:
		print('Everything is Fine')
	time.sleep(1)
	sys.stdout.flush()
	n += 1
