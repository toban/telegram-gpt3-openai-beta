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
		self.default_agent_description = 'The assistant is helpful, creative, clever, and very friendly.'
		self.default_messages = [
			'Human: Hello, who are you?',
			'AI: I am an AI created by OpenAI. How can I help you today?',
		]
		openai.api_key = token
		self.intro ='The following is a conversation with an AI assistant.'
		self.agent_description=self.default_agent_description



	def getCompletionResponse(self, response):
		self.logger.info(response)
		if len(response['choices']) == 1:
			return response['choices'][0]['text']
		else:
			self.logger.info("Got more than one response!")
			return response['choices'][0]['text']

	def setAgentDescription(self, description):
		self.agent_description = description

	def sendRequest(self, userText, messages):

		userMessage = 'Human: ' + userText
		botCompletion = 'AI:'

		# append messages
		messages.append(userMessage)
		messages.append(botCompletion)

		lastPos = len(messages) - 1 

		prompt = self.intro + " " + self.agent_description + "\n\n" + '\n'.join(messages)

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

		responseMessage = self.getCompletionResponse(response)
		messages[lastPos] = messages[lastPos] + responseMessage

		return responseMessage, messages

