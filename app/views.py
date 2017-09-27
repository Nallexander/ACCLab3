from app import app
from flask import Flask, jsonify, request
from read_data_celery import countPronouns
from time import sleep

@app.route('/', methods=['GET'])
@app.route('/index/', methods=['GET'])
def index():
	data = request.get_json()
	file = data.get('file')
	print('hej')
	pronouns = countPronouns.delay(file)
	print('hoj')
	# print(pronouns)
	# return pronouns
	# sleep()
	while not pronouns.ready():
		sleep(0.5)
		result = pronouns.result
		print(result)
		return(result)