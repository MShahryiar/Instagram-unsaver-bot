from unsave import Unsave
import constants as consts

with Unsave() as bot:
	bot.land_first_page()
	bot.login(consts.username,consts.password)