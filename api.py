import logging
import time
import sys
from config import Setup
import os
import openai

class Api:

	def __init__(self, token=Setup.config['open_api_key']):

		self.logger = logging.getLogger('Api')
		self.token = token
		openai.api_key = token


	def sendRequest(self, userText):

		userMessage = 'Human: ' + userText
		intro='The following is a conversation with an AI assistant.'
		agent_description='The assistant is helpful, creative, clever, and very friendly.'

		botCompletion = 'AI:'

		messages = [
			'Human: Hello, who are you?',
			'AI: I am an AI created by OpenAI. How can I help you today?',
			userMessage,
			botCompletion
		]


		prompt = intro + " " + agent_description + "\n\n" + '\n'.join(messages)

		#self.logger.info("sending:\n" + prompt )
		response = openai.Completion.create(
		  engine="davinci",
		  prompt=prompt,
		  temperature=0.9,
		  max_tokens=150,
		  top_p=1,
		  frequency_penalty=0.0,
		  presence_penalty=0.6,
		  stop=["\n", " Human:", " AI:"]
		)


		self.logger.info(response)
		if len(response['choices']) == 1:
			return response['choices'][0]['text']
		else:
			self.logger.info("Got more than one response!")
			return response['choices'][0]['text']

