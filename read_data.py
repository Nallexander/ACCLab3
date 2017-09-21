import os
import json

my_dir = "/Users/Alex/Dropbox/Programmering/Cloud/Lab3/data/"
os.chdir(my_dir)
with open("f09905c6-161d-4ca1-9ef2-7af7441f9a1a") as json_data:
	d = json.load(json_data)
	print(d)

