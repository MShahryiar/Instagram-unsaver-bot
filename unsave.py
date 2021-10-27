import constants as consts
import os 
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Unsave(webdriver.Chrome):
	def __init__(self, driver_path=r'E:/Programming_Stuff/Selenium_WebScraping/Final-insta-bot-git/Instagram-unsaver-bot',teardown = False):
		self.driver_path = driver_path
		self.teardown = teardown
		os.environ["PATH"] += os.pathsep + driver_path
		options = webdriver.ChromeOptions()
		options.add_experimental_option('excludeSwitches',['enable-logging']) # used to ignoring warning msgs in CLI
		super(Unsave, self).__init__(options=options)
		self.implicitly_wait(15)
		self.maximize_window() 

	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.teardown:
			self.quit()

	def land_first_page(self):
		self.get(consts.BASE_URL)

	def login(self,username, password):
		# enter login details and go to main page
		username_input = self.find_element_by_css_selector(
			'input[name="username"]'
			)
		username_input.clear()
		username_input.send_keys(username)

		password_input = self.find_element_by_css_selector(
			'input[name="password"]'
			)
		password_input.clear()
		password_input.send_keys(password)


		submit_btn = self.find_element_by_css_selector(
			'button[type="Submit"]'
			).click()
	
	def no_notifications(self):
		self.find_element_by_class_name('HoLwm').click()


	def go_to_profile(self,username):
		self.get(f'https://www.instagram.com/{username}/saved/')


	def saved_Items(self):
		counter = 0
		while True:
			try:
				saved_item = self.find_element_by_class_name(
				'v1Nh3').click()
				unsave = self.find_element_by_css_selector(
					'svg[aria-label="Remove"]').click()
				close_item = self.find_element_by_css_selector(
				'svg[aria-label="Close"]').click()
				counter += 1
				self.refresh()
			except:
				print(f'Finished Unsaving posts! Total Unsaved posts => {counter}')
				break



		

	def output(self):
		pass 
		# After all of the items have been unsaved.
		# Show in nice format, how many have been deleted


	
