from read_data_celery import countPronouns
pronouns = countPronouns.delay('f1c47aa7-5b69-4467-897c-24151649bcf4')
while True:
	if pronouns.ready():
		break
print(pronouns.get())