import requests

import logging
logging.basicConfig(level=logging.DEBUG)

import json

HEADERS = {
	'Access-Control-Allow-Origin': '*',
	'Access-Control-Allow-Methods': 'GET',
	'Access-Control-Allow-Headers': 'Content-Type',
	'Access-Control-Max-Age': '3600',
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

# Event: JSON with event object
# Context: Not used (https://docs.aws.amazon.com/lambda/latest/dg/python-context.html)
def lambda_handler(event, context):
	logging.info(event)
	logging.info(context)

	statusCode = 200

	try:
		# Make request to JSON API
		URL = "https://jsonplaceholder.typicode.com/posts/1/comments"
		PAYLOAD = {}
		req = requests.get(URL, headers=HEADERS, params=PAYLOAD)
		if req.status_code == 200:
			# Convert content to JSON
			jsonObj = json.loads(req.content.decode("utf-8"))
			# Print all posts
			for post in jsonObj:
				logging.info(post["email"])
		else:
			statusCode = req.status_code
			logging.error("Unsuccessful API call ({0})".format(statusCode))

	except Exception as e:
		logging.error(str(e))

	# Return result to AWS Lambda
	return {
		'statusCode': statusCode,
		'body': json.dumps('Finished')
	}