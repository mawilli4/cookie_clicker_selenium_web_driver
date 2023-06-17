from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)

click = "TRUE"
clicks = 0
driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()
cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")


def check_upgrades():
	available_upgrade = []
	cookie_count = int(driver.find_element(By.CSS_SELECTOR, "#money").text.replace(",", ""))
	cursor_cost = int(driver.find_element(By.CSS_SELECTOR, "#buyCursor b").text[9:].replace(",", ""))
	grandma_cost = int(driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").text[10:].replace(",", ""))
	factory_cost = int(driver.find_element(By.CSS_SELECTOR, "#buyFactory b").text[10:].replace(",", ""))
	mine_cost = int(driver.find_element(By.CSS_SELECTOR, "#buyMine b").text[7:].replace(",", ""))
	shipment_cost = int(driver.find_element(By.CSS_SELECTOR, "#buyShipment b").text[11:].replace(",", ""))
	alchemy_cost = int(driver.find_element(By.ID, 'buyAlchemy lab').text[14:].replace(",", "").split("\n")[0])
	portal_cost = int(driver.find_element(By.CSS_SELECTOR, "#buyPortal b").text[9:].replace(",", ""))
	time_cost = int(driver.find_element(By.ID, 'buyTime machine').text[15:].replace(",", "").split("\n")[0])
	elder = driver.find_element(By.ID, 'buyElder Pledge')
	elder_display = driver.find_element(By.XPATH, '//*[@id="buyElder Pledge"]').get_attribute("style").split(";")[0]
	if elder_display != "display: none":
		elder.click()
	print(cursor_cost, grandma_cost, factory_cost, mine_cost, shipment_cost, alchemy_cost, portal_cost, time_cost)
	if cookie_count > cursor_cost:
		available_upgrade.append(cursor_cost/0.2)
	if cookie_count > grandma_cost:
		available_upgrade.append(grandma_cost)
	if cookie_count > factory_cost:
		available_upgrade.append(factory_cost/4)
	if cookie_count > mine_cost:
		available_upgrade.append(mine_cost/10)
	if cookie_count > shipment_cost:
		available_upgrade.append(shipment_cost/20)
	if cookie_count > alchemy_cost:
		available_upgrade.append(alchemy_cost/100)
	if cookie_count > portal_cost:
		available_upgrade.append(portal_cost / 1333)
	if cookie_count > time_cost:
		available_upgrade.append(time_cost / 10000)
	print(available_upgrade, min(available_upgrade))
	if cursor_cost/0.2 == min(available_upgrade):
		cursor = driver.find_element(By.CSS_SELECTOR, "#buyCursor")
		cursor.click()
		available_upgrade = [1]
	if grandma_cost == min(available_upgrade):
		grandma = driver.find_element(By.CSS_SELECTOR, "#buyGrandma")
		grandma.click()
		available_upgrade = [1]
	if factory_cost/4 == min(available_upgrade):
		factory = driver.find_element(By.CSS_SELECTOR, "#buyFactory")
		factory.click()
		available_upgrade = [1]
	if mine_cost/10 == min(available_upgrade):
		mine = driver.find_element(By.CSS_SELECTOR, "#buyMine")
		mine.click()
		available_upgrade = [1]
	if shipment_cost/20 == min(available_upgrade):
		shipment = driver.find_element(By.CSS_SELECTOR, "#buyShipment")
		shipment.click()
		available_upgrade = [1]
	if alchemy_cost/100 == min(available_upgrade):
		alchemy = driver.find_element(By.ID, 'buyAlchemy lab')
		alchemy.click()
		available_upgrade = [1]
	if portal_cost/1333 == min(available_upgrade):
		portal = driver.find_element(By.CSS_SELECTOR, "#buyPortal")
		portal.click()
		available_upgrade = [1]
	if time_cost/10000 == min(available_upgrade):
		time = driver.find_element(By.ID, 'buyTime machine')
		time.click()
		available_upgrade = [1]


while click:
	cookie.click()
	clicks += 1
	if clicks < 6000 and clicks % 280 == 0:
		print(clicks)
		check_upgrades()
	if 6000 <= clicks < 30000 and clicks % 560 == 0:
		print(clicks)
		check_upgrades()
	if 30000 <= clicks < 300000 and clicks % 2240 == 0:
		print(clicks)
		check_upgrades()
	if 300000 <= clicks and clicks % 17920 == 0:
		print(clicks)
		check_upgrades()
