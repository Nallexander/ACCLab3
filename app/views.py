from flask import Flask, jsonify, request
from .. import read_data_celery
from time import sleep

@app.route('/', methods=['GET'])
@app.route('/index/', methods=['GET'])
def index():
	data = request.get_json()
	file = data.get('file')
	pronouns = read_data_celery.countPronouns.delay(file)
	# print(pronouns)
	# return pronouns
	# sleep()
	while pronouns.ready() == False:
		sleep(0.5)
	print('klar')
	print(pronouns.ready())
	result = pronouns.result
	print(result)
	return('hej')