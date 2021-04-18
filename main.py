import logging
import time
import sys
from config import Setup
import os
from bot import Bot

logfile = None if 'logfile' not in Setup.config else Setup.config['logfile']
logging.basicConfig(filename=logfile, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger('Main')


bot = Bot(Setup.config['bot_token'], Setup.config['bot_name'], Setup.config['voice_pitch']) 


while True:
	try:
		bot.update()
	except:

		e = sys.exc_info()[0]
		logger.error(e)
		time.sleep(10)

