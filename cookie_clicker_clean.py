import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

CURSOR_RATE = 0.2
GRANDMA_RATE = 1
FACTORY_RATE = 4
MINE_RATE = 10
SHIPMENT_RATE = 20
ALCHEMY_LAB_RATE = 100
PORTAL_RATE = 1333.2
TIME_MACHINE_RATE = 24691.2

cursor = {}
grandma = {}
factory = {}
mine = {}
shipment = {}
alchemy = {}
portal = {}
time = {}
full_dict = {}
elder_display = " "
big_number = 999999999


def elder():
	global elder_display
	try:
		elder = driver.find_element(By.ID, 'buyElder Pledge')
		elder_display = driver.find_element(By.ID, 'buyElder Pledge').get_attribute("style").split(";")[0].split(":")[1][1:]
		if elder_display != "none":
			elder.click()
	except:
		pass


def cursor_scrape():
	global cursor, full_dict, big_number
	try:
		cursor_cost = int(driver.find_element(By.CSS_SELECTOR, "#buyCursor b").text[9:].replace(",", ""))
		cursor_value = cursor_cost / CURSOR_RATE
		cursor_element = driver.find_element(By.CSS_SELECTOR, "#buyCursor")
		cursor = {"value": cursor_value, "element": cursor_element}
		full_dict[0] = cursor
	except selenium.common.exceptions.StaleElementReferenceException:
		full_dict[0] = {"value": big_number}


def grandma_scrape():
	global grandma, full_dict
	try:
		grandma_cost = int(driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").text[10:].replace(",", ""))
		grandma_value = grandma_cost / GRANDMA_RATE
		grandma_element = driver.find_element(By.CSS_SELECTOR, "#buyGrandma")
		grandma = {"value": grandma_value, "element": grandma_element}
		full_dict[1] = grandma
	except:
		full_dict[1] = {"value": big_number}


def factory_scrape():
	global factory, full_dict
	try:
		factory_cost = int(driver.find_element(By.CSS_SELECTOR, "#buyFactory b").text[10:].replace(",", ""))
		factory_value = factory_cost / FACTORY_RATE
		factory_element = driver.find_element(By.CSS_SELECTOR, "#buyFactory")
		factory = {"value": factory_value, "element": factory_element}
		full_dict[2] = factory
	except:
		full_dict[2] = {"value": big_number}


def mine_scrape():
	global mine, full_dict
	try:
		mine_cost = int(driver.find_element(By.CSS_SELECTOR, "#buyMine b").text[7:].replace(",", ""))
		mine_value = mine_cost / MINE_RATE
		mine_element = driver.find_element(By.CSS_SELECTOR, "#buyMine")
		mine = {"value": mine_value, "element": mine_element}
		full_dict[3] = mine
	except:
		full_dict[3] = {"value": big_number}


def shipment_scrape():
	global shipment, full_dict
	try:
		shipment_cost = int(driver.find_element(By.CSS_SELECTOR, "#buyShipment b").text[11:].replace(",", ""))
		shipment_value = shipment_cost / SHIPMENT_RATE
		shipment_element = driver.find_element(By.CSS_SELECTOR, "#buyShipment")
		shipment = {"value": shipment_value, "element": shipment_element}
		full_dict[4] = shipment
	except:
		full_dict[4] = {"value": big_number}


def alchemy_scrape():
	global alchemy, full_dict
	try:
		alchemy_cost = int(driver.find_element(By.ID, 'buyAlchemy lab').text[14:].replace(",", "").split("\n")[0])
		alchemy_value = alchemy_cost / ALCHEMY_LAB_RATE
		alchemy_element = driver.find_element(By.ID, 'buyAlchemy lab')
		alchemy = {"value": alchemy_value, "element": alchemy_element}
		full_dict[5] = alchemy
	except:
		full_dict[5] = {"value": big_number}


def portal_scrape():
	try:
		global portal, full_dict
		portal_cost = int(driver.find_element(By.CSS_SELECTOR, "#buyPortal b").text[9:].replace(",", ""))
		portal_value = portal_cost / PORTAL_RATE
		portal_element = driver.find_element(By.CSS_SELECTOR, "#buyPortal")
		portal = {"value": portal_value, "element": portal_element}
		full_dict[6] = portal
	except:
		full_dict[6] = {"value": big_number}


def time_scrape():
	global time, full_dict
	try:
		time_cost = int(driver.find_element(By.ID, 'buyTime machine').text[15:].replace(",", "").split("\n")[0])
		time_value = time_cost / TIME_MACHINE_RATE
		time_element = driver.find_element(By.ID, 'buyTime machine')
		time = {"value": time_value, "element": time_element}
		full_dict[7] = time
	except:
		full_dict[7] = {"value": big_number}


click = "TRUE"
clicks = 0

while click:
	value_list = []
	elder()
	try:
		cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
		cookie.click()
		clicks += 1
		cookie_count = int(driver.find_element(By.CSS_SELECTOR, "#money").text.replace(",", ""))
	except:
		pass
	cursor_scrape()
	grandma_scrape()
	factory_scrape()
	mine_scrape()
	shipment_scrape()
	alchemy_scrape()
	portal_scrape()
	time_scrape()
	for item in full_dict:
		value_list.append(full_dict[item]["value"])
	best_value = min(value_list)
	print(clicks, value_list, best_value)
	for item in full_dict:
		if full_dict[item]["value"] == best_value:
			try:
				full_dict[item]["element"].click()
			except:
				pass
