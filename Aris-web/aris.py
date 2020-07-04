import time
import sys

def fn():
	n = 1
	while(True):
		s = ""
		if(n % 10 == 0):
			s = "Accident Detected"
			print("Accident Detected")
			sys.stdout.flush()
			time.sleep(1)
		else:
			print("Everything is fine")
			s = "Everything is fine"
			sys.stdout.flush()
			time.sleep(1)
		n += 1
	
fn()