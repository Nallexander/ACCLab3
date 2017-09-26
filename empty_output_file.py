import json
with open('output.json','w') as file:
	pronoun_count = {'han': 0, 'hon': 0, 'den': 0, 'det': 0, 'denna': 0, 'hen': 0}
	json.dump(pronoun_count,file)