from telegram import Update
import logging
import telegram
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters, CallbackContext
import time
import sys
from config import Setup
import os
from api import Api
import time


## todo telegram.vendor.ptb_urllib3.urllib3.exceptions.ReadTimeoutError:
## todo telegram.error.BadRequest: Message must be non-empty

class Bot:

	def __init__(self, token, name, voice_pitch):


		self.logger = logging.getLogger('Bot: ' + name)
		self.logger.info("starting bot! " + token[0:4])

		self.api = Api()
		self.messages = self.api.default_messages

		self.updater = Updater(token=token, use_context=True)

		self.dispatcher = self.updater.dispatcher
		self.dispatcher.add_handler(MessageHandler(Filters.chat(Setup.config['chat_id']) & Filters.text & ~Filters.command, self.messageHandler))
		self.updater.start_polling()

		self.name = name
		self.last_time = None
		self.voice_pitch = voice_pitch
		self.talk(self.api.intro + "\n\n" + self.api.agent_description)



	def send_voice(self, message):
		self.logger.info("send voice: " + message)
		try:
			# vorbis-tools
			os.system('espeak "' + message + '" -v sv -p '+ str(self.voice_pitch) +' -s 100 --stdout | oggenc -b 50 -o out.ogg -')
			voice = open('out.ogg', 'rb')
			self.dispatcher.bot.send_voice(Setup.config['chat_id'], voice, None, message)
			os.system('rm -f out.ogg')
		except: # catch all
			e = sys.exc_info()[0]
			self.logger.error(e)
			raise e

	def talk(self, message, reply_message=None):
		self.logger.info(message)
		try:
			if reply_message is not None:
				self.dispatcher.bot.send_message(chat_id=Setup.config['chat_id'], text=message)#, reply_to_message_id=reply_message.message_id)
			else:
				self.dispatcher.bot.send_message(chat_id=Setup.config['chat_id'], text=message, disable_notification=True)
		except telegram.error.TimedOut:
			self.logger.error("timeout!")
			time.sleep(10)
		except: # catch all
			e = sys.exc_info()[0]
			self.logger.error(e)
			raise e

	def messageHandler(self, update: Update, context: CallbackContext) -> None:

		# todo ignore really old messages

		text = update.message.text
		user = update.message.from_user

		self.logger.info(user.first_name + " " + user.last_name + ": " + text)

		if text.startswith( '!clear' ):
			self.clearMessages()
			return

		if text.startswith( '!set_agent_description=' ):
			segments = text.split("=")
			description=segments[1]

			if description == None or len(segments) == 1:
				description = self.api.default_agent_description
		
			self.api.setAgentDescription(description)
			self.logger.info("setting agent description: " + description)
			self.talk("setting agent description: " + description)
			return

		responseMessage, messages = self.api.sendRequest(text, self.messages)
		self.messages = messages

		self.talk(responseMessage)
		self.last_time = int(round(time.time() * 1000))

	def clearMessages(self): 
		self.logger.info("clearing messages")
		self.messages = self.api.default_messages
		self.talk("How can i help you?")
		self.last_time = None

	def update(self):

		if self.last_time != None:
			now = int(round(time.time() * 1000))
			diff = now - self.last_time
			self.logger.info(diff)

			if diff > 1000 * 60:
				self.clearMessages()
				return


		#self.talk(trimmed, self.reply_message)
		time.sleep(10)

