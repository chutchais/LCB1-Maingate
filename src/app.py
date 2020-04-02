from flask import Flask,jsonify,render_template
import requests

app = Flask(__name__)

URL_MAINGATE = 'http://www.truckq_api.laemchabangport.com:8043/TQ_API_TLC/api/TLC_Gatein/getDetail'


@app.route('/')
@app.route('/<terminal>')
def hello_world(terminal='B1'):
	from datetime import datetime
	now = datetime.now() # current date and time
	date_time = now.strftime("%Y-%m-%d")

	a0_json ={
	"User":"lcba0adm",
	"Password":"P@55w0rd",
	"Start_Date":"%s 00:00:00" % date_time,
	"End_Date": "%s 23:59:59" % date_time
	}

	b1_json ={
		"User":"lcbb1adm",
		"Password":"P@55w0rd",
		"Start_Date":"%s 00:00:00" % date_time,
		"End_Date":	"%s 23:59:59" % date_time
	}
	url = a0_json if terminal == 'A0' else b1_json
	res = requests.post(URL_MAINGATE,url)
	# return 'Ok' if res.ok else 'Failed'
	# return jsonify(res.json())
	# '.decode('utf8')'
	return render_template('maingate.html', trucks=res.json() ,terminal=terminal,report_date=date_time)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)