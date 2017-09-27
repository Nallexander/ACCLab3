from app import app
from flask import Flask, jsonify, request

@app.route('/')
@app.route('/index/<uuid>', methods=['GET'])
def index():
	data = request.get_json()
	file = data.get('file')
	
	return message
