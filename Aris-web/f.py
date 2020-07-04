from flask import Flask,render_template,send_from_directory
import time

app = Flask(__name__, template_folder='web',static_url_path='',static_folder='web')


@app.route('/')
def index(): 
	return render_template('index.html', ent_direc ="120")

def fn():
	n = 1
	while(True):
		s = ""
		if(n % 10 == 0):
			s = "Accident Detected"
			return s
			time.sleep(1)
		else:
			s = "Everything is fine"
			return s
			time.sleep(1)
		n += 1

@app.route('/update', methods= ['GET'])
def stuff():
    s=fn()
    return jsonify(s=s)

if __name__ == '__main__':
	app.run(debug = True)