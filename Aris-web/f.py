from flask import Flask,render_template, send_from_directory,  url_for, copy_current_request_context,jsonify
from time import sleep
from threading import Thread, Event
from queue import Queue
from flask_socketio import SocketIO, emit
from glob import glob
from os import path
from multiprocessing import Process
import requests
#from engineio.async_drivers import gevent
#import jinja2

def send_sms():
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=ARIS&message='\nAccident Detected \n\n Vehicle No : TN 45 AA 5797 \n\n Date and Time: 16:07, 3 AUG 2020\n\n Location: Asthampatty,Salem,TamilNadu\n\n Spot (GPS Hashcode): tdpd6hk7qhsp'&language=english&route=p&numbers=7010406958"
    headers = {'authorization': "jG6FRZkW9h0DoqUdAcsaIumEyBgbNlwTYrCMvHK3izP1x4V5JXGCNMdmAPV2le1QI03BjgUFOESviqHn",'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache",}
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    
"""import os, sys
base_dir = '.'
if hasattr(sys, '_MEIPASS'):
    base_dir = os.path.join(sys._MEIPASS)

app = Flask(__name__,
        static_folder=os.path.join(base_dir, 'static'),
        template_folder=os.path.join(base_dir, 'templates'))"""

q = Queue()
app = Flask(__name__)
stat = "Everything is fine"
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
db_acc = [
                     ["TN 27 AC 5678",
                     "16:03, 3 AUG 2020",
                     "Four-Roads",
                     "qtd6hk7qhsp",
                     "9865445476"],
                
                     ["TN 45 BZ 2658",
                     "16:04, 3 AUG 2020",
                     "Seelanayakanpatty",
                     "aod6hk7qhsp",
                     "8865634728"]
          ]

db_up_acc = [
                     ["TN 27 AC 5678",
                     "16:03, 3 AUG 2020",
                     "Four-Roads",
                     "qtd6hk7qhsp",
                     "9865445476"],
                
                     ["TN 45 BZ 2658",
                     "16:04, 3 AUG 2020",
                     "Seelanayakanpatty",
                     "aod6hk7qhsp",
                     "8865634728"],

                     ["TN 45 AA 5797",
                     "16:07, 3 AUG 2020",
                     "Asthampatty",
                     "tdpd6hk7qhsp",
                     "7010406958"]
                     
          ]


#turn the flask app into a socketio app
socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)

#status thread
thread = Thread()
thread_stop_event = Event()
"""
def server():
	from http.server import SimpleHTTPRequestHandler
	from socketserver import TCPServer
	PORT = 1000
	DIRECTORY = "d:\\Acc\\"

	class Handler(SimpleHTTPRequestHandler):
		def __init__(self, *args, **kwargs):
			super().__init__(*args, directory=DIRECTORY, **kwargs)

	with TCPServer(("", PORT), Handler) as httpd:
		print("serving at port", PORT)
		httpd.serve_forever()

process = Process(target=server)

def proc_init():
	global process
	print("process intiate \n\n\n")
	process = Process(target=server)
"""
def fn():
	global stat
	n = 1
	while(True):
		if(n % 20 == 0):
			stat = "Accident Detected"
			q.put(stat)
			sleep(1)
		else:
			stat = "Everything Fine"
			sleep(1)
		n += 1
		#print(s)
def ack(value):
    if value != 'pong':
    	None
    	
def update():
	global q
	while not thread_stop_event.isSet():
		if(q.empty()):
			st = "Everything Fine"
			#print(st)
			socketio.emit('newnumber', {'number': st}, namespace='/update')
			socketio.sleep(1)
		else:
			st = str(q.get())
			#print(st)
			socketio.emit('newnumber', {'number': st}, namespace='/update')
			socketio.sleep(1)

@app.route('/')
def home():
	global thread_stop_event
	#global process
	thread_stop_event.set()
	"""if process.is_alive():
		print("process closes \n\n\n")
		process.terminate()
		proc_init()"""
	#print("close\n\n")
	return render_template('index.html', ent_direc ="120")

@app.route('/index.html/')
def index(): 
	global thread_stop_event
	#global process
	thread_stop_event.set()
	"""if process.is_alive():
		print("process closes \n\n\n")
		process.terminate()
		proc_init()"""
	#print("close\n\n")
	return render_template('index.html', ent_direc ="120")

@app.route('/products.html/')
def products():
    send_sms()
	#global process
	# """if process.is_alive():
	# 	print("process closes \n\n\n")
	# 	process.terminate()
	# 	proc_init()"""
    return render_template('products.html', ent_direc ="120")

@app.route('/gallery.html/')
def gallery(): 
	global thread_stop_event
	#global process
	thread_stop_event.set()
	#print("close\n\n")
	"""if process.is_alive():
		print("process closes \n\n\n")
		process.terminate()
		proc_init()
	process.start()"""
	gallery_list = glob("d:\\Acc\\*.mp4")
	#python -m http.server 9000
	for i in range(0,len(gallery_list)):
		gallery_list[i] = path.basename(str(gallery_list[i]))

	return render_template('gallery.html', gallery_list = gallery_list, ent_direc ="120")

@app.route('/cctv.html/')
def cctv(): 
	global thread_stop_event
	thread_stop_event.set()
	"""if process.is_alive():
		print("process closes \n\n\n")
		process.terminate()
		proc_init()"""
	#print("close\n\n")
	return render_template('cctv.html', ent_direc ="120")
		
@socketio.on('connect', namespace='/update')
def test_connect():
    # need visibility of the global thread object
    global thread
    global thread_stop_event
    thread_stop_event.clear() 
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = socketio.start_background_task(update)

@app.route("/update-acc-table/", methods=["GET", "POST"])
def update_acc_table():
	s = """
                <thead>
                  <tr>
                    <th scope="col">&nbsp;</th>
                    <th scope="col">Vehicle No</th>
                    <th scope="col">Date & Time</th>  
                    <th scope="col">Location</th>
                    <th scope="col">Spot</th>
                    <th scope="col">Mobile No</th>
                    <!--<th scope="col">&nbsp;</th>-->
                  </tr>
                </thead>
                <tbody>
	"""

	for i,val1 in enumerate(db_up_acc):
		s += """ <tr>
                    <th scope="row"><input type="checkbox" /></th>
              """
		for j,val2 in enumerate(db_up_acc[i]):
			s += "<td>"+str(db_up_acc[i][j])+"</td>"
		s += "</tr>"
	#s = "<thead><tr><th scope=\"col\">&nbsp;</th><th scope=\"col\">Vehicle No</th><th scope=\"col\">Date & Time</th>  <th scope=\"col\">Location</th><th scope=\"col\">Spot</th><th scope=\"col\">Mobile No</th><!--<th scope=\"col\">&nbsp;</th>--></tr></thead><tbody><tr><th scope=\"row\"><input type=\"checkbox\" /></th><td>TN 27 AC 5678</td><td>17:30, 12 FEB 2020</td><td>Four-Roads</td><td>Pole 15</td><td>9865445476</td></tr>"
	return jsonify({'s':s})

"""@socketio.on('disconnect', namespace='/update')
def test_disconnect():
    global thread_stop_event
    thread_stop_event.set() 
    print('Client disconnected')"""

if __name__ == '__main__':

	t1 = Thread(target=fn)
	t1.start()
	#proc_init()
	#app.run(debug = True)
	socketio.run(app)
	t1.join()