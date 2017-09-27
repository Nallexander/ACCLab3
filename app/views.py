from app import app
from flask import Flask, jsonify, request

@app.route('/')
@app.route('/index/<uuid>', methods=['POST'])
def index():
	request_json = request.get_json()
	message = request_json.get('message')
	return message
