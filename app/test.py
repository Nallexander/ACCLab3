from flask import Flask, jsonify, request
from read_data_celery import countPronouns
from time import sleep

def index():
	data = request.get_json()
	file = data.get('file')
	print('hej')
	pronouns = countPronouns.delay(file)
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