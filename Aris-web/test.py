import time
import eel



eel.init('web')

@eel.expose
def fn():
	n = 1
	print("hi")
	s = ""
	if(n % 10 == 0):
		s = "Accident Detected"
		return s
		#print("Accident Detected")
	else:
		#print("Everything is fine")
		s = "Everything is fine"
		
	n += 1
	return s

eel.start('index.html', size=(1000,600))
