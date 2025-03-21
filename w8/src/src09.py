import requests
import json



try:

	baseUrl = 'http://localhost:5000/api/peoplefull'
	headers = {'content-type': 'application/json'}
	
	
	
	# get all
	response = requests.get(baseUrl)
	print('GET: {}'.format(response.status_code))
	peoples = json.loads(response.content)
	
	for people in peoples:
	
		print(people)
	
	
	
	# get one
	response = requests.get(baseUrl + '/Brockman')
	print('GET: {}'.format(response.status_code))
	people = json.loads(response.content)

	print(people)
	
	
	
	# put
	newPeople = {'fname': 'Donald', 'lname': 'Trump'}
	response = requests.put(baseUrl, headers = headers, data = json.dumps(newPeople))
	print('PUT: {}'.format(response.status_code))
	
	
	
	# get all
	response = requests.get(baseUrl)
	print('GET: {}'.format(response.status_code))
	peoples = json.loads(response.content)
	
	for people in peoples:
	
		print(people)
	
	
	
	# post
	newPeople['fname'] = 'Joe'
	response = requests.post(baseUrl + '/' + newPeople['lname'], headers = headers, data = json.dumps(newPeople))
	print('POST: {}'.format(response.status_code))
	
	
	
	# get all
	response = requests.get(baseUrl)
	print('GET: {}'.format(response.status_code))
	peoples = json.loads(response.content)
	
	for people in peoples:
	
		print(people)
	
	
	
	# delete	
	response = requests.delete(baseUrl, headers = headers, params={'lname':newPeople['lname']})
	print('DELETE: {}'.format(response.status_code))
	
	
	
	# get all
	response = requests.get(baseUrl)
	print('GET: {}'.format(response.status_code))
	peoples = json.loads(response.content)
	
	for people in peoples:
	
		print(people)



except:

	print('********** UNKNOWN ERROR')
