from celery import Celery
import os
import json


def cleanString(string):
	filtered = string.replace(',', '')
	filtered = filtered.replace('.', '')
	filtered = filtered.replace('!', '')
	filtered = filtered.replace('?', '')
	filtered = filtered.replace(')', '')
	filtered = filtered.lower()
	return filtered

def registerPronoun(string, pronoun_count):
	han = len([x for x in string.split() if x == 'han'])
	hon = len([x for x in string.split() if x == 'hon'])
	den = len([x for x in string.split() if x == 'den'])
	det = len([x for x in string.split() if x == 'det'])
	denna = len([x for x in string.split() if x == 'denna'])
	hen = len([x for x in string.split() if x == 'hen'])

	pronoun_count['han'] += han
	pronoun_count['hon'] += hon
	pronoun_count['den'] += den
	pronoun_count['det'] += det
	pronoun_count['denna'] += denna
	pronoun_count['hen'] += hen

#from https://stackoverflow.com/questions/5508509/how-do-i-check-if-a-string-is-valid-json-in-python
def isJson(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError, e:
    return False
  return True

app = Celery('tasks', backend='rpc://', broker='pyamqp://')

@app.task
def countPronouns(dir, file):
	my_dir = dir
	#"/Users/Alex/Dropbox/Programmering/Cloud/Lab3/data/"
	os.chdir(my_dir)

	with open(file) as json_data:
		pronoun_count = {'han': 0, 'hon': 0, 'den': 0, 'det': 0, 'denna': 0, 'hen': 0}
		for json_line in json_data:
			if isJson(json_line):
				d = json.loads(json_line)
				cleaned_string = cleanString(d['text'])
				
				registerPronoun(cleaned_string, pronoun_count)
		print(pronoun_count)