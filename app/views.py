from app import app
from flask import Flask, jsonify, request
from time import sleep

@app.route('/', methods=['GET'])
@app.route('/index/', methods=['GET'])
def index():
	data = request.get_json()
	file = data.get('file')
	print('hej')
	pronouns = app.read_data_celery.countPronouns.delay(file)
	print('hoj')
	# print(pronouns)
	# return pronouns
	# sleep()
	# while not pronouns.ready():
	sleep(8)
	if pronouns.ready():
		result = pronouns.get(timeout=1)
		print(result)
		return("Klar")
	else:
		return("Inte klar")