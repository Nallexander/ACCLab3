from app import app
from flask import Flask, jsonify, request

@app.route('/')
@app.route('/index/<uuid>', methods=['POST'])
def index(uuid):
	request_json = request.get_json()
	message = request_json.get('message')
	print(uuid)
	return uuid
