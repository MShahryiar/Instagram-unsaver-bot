from unsave import Unsave
import constants as consts

with Unsave() as bot:
	bot.land_first_page()
	bot.login(consts.username,consts.password)
	bot.no_notifications()
	bot.go_to_profile(consts.username)
