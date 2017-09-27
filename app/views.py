from app import app
from flask import Flask, jsonify, request
from read_data_celery import countPronouns

@app.route('/', methods=['GET'])
@app.route('/index/', methods=['GET'])
def index():
	data = request.get_json()
	file = data.get('file')
	pronouns = countPronouns.delay(file)
	# print(pronouns)
	# return pronouns

	while not pronouns.ready():
		true
	return(pronouns)
