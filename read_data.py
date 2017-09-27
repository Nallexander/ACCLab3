import os
import json


# def cleanString(string):
# 	filtered = string.replace(',', '')
# 	filtered = filtered.replace('.', '')
# 	filtered = filtered.replace('!', '')
# 	filtered = filtered.replace('?', '')
# 	filtered = filtered.replace(')', '')
# 	filtered = filtered.lower()
# 	return filtered

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

def updateJsonFile(pronoun_count):
	with open('output.json', 'r') as json_output:
		data = json.load(json_output)
	data['han'] = pronoun_count['han'] + data['han']
	data['hon'] = pronoun_count['hon'] + data['hon']
	data['den'] = pronoun_count['den'] + data['den']
	data['det'] = pronoun_count['det'] + data['det']
	data['denna'] = pronoun_count['denna'] + data['denna']
	data['hen'] = pronoun_count['hen'] + data['hen']
	with open('output.json', 'w+') as json_output:
		json.dump(data, json_output)





my_dir = "/Users/Alex/Dropbox/Programmering/Cloud/Lab3/data/"
os.chdir(my_dir)
pronoun_count = {'han': 0, 'hon': 0, 'den': 0, 'det': 0, 'denna': 0, 'hen': 0}
no_of_tweets = 0
for filename in os.listdir(os.getcwd()):
	with open(filename) as json_data:	
		for json_line in json_data:
			if isJson(json_line):
				tweet = json.loads(json_line)
				# cleaned_string = cleanString(d['text'])

				if not tweet['retweeted']:
					no_of_tweets += 1
					registerPronoun(tweet['text'], pronoun_count)
print(pronoun_count)
print(no_of_tweets)
my_dir2 = "/Users/Alex/Dropbox/Programmering/Cloud/Lab3/"
os.chdir(my_dir2)
updateJsonFile(pronoun_count)




	# print(d['text'].find(' hen '))




