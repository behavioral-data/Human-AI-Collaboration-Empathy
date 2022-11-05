import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
CORS(app)

import json


@app.route('/api/rewriting', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def api_all():
	if request.method == "POST": 
		curr_post = request.json #request.args['SP']
		# print(curr_post)

		seeker_post = curr_post['SP']
		response_post = curr_post['RP']

		seeker_post = seeker_post.strip().lower()
		response_post = response_post.strip().lower()

		if seeker_post.strip() == "my job is becoming more and more stressful with each passing day." and response_post.strip() == "don't worry! i'm there for you.":
			output_response_li_op = []

			output_response_li_op.append({'operation': '<REPLACE>', 'sentence': "It must be a real struggle!", 'old_sentence': "Don't worry!"})
			output_response_li_op.append({'operation': '<NOOP>', 'sentence': "I'm there for you."})
			output_response_li_op.append({'operation': '<INSERT>', 'sentence': 'Have you tried talking to your boss?'})
		
		return jsonify({'op': output_response_li_op})

app.run(debug=True, host="localhost", port=10000)