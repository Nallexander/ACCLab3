from flask import Flask, jsonify, request
from read_data_celery import countPronouns
from time import sleep
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/index/', methods=['GET'])
def index():
	data = request.get_json()
	jsonfile = data.get('file')
	pronouns = countPronouns.delay(jsonfile)
	# print(pronouns)
	# return pronouns
	# sleep()
	while pronouns.ready() == False:
		sleep(0.5)
	print('klar')
	print(pronouns.ready())
	result = pronouns.result
	print(result)
	return(json.dumps(result))

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)