from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import timeit
import wget

def page1():
	myURL = input("Please enter the link and press ENTER. \n")
	#Timer Starts
	start = timeit.default_timer()

	# instantiate a chrome options object so you can set the size and headless preference
	chrome_options = Options()

	#chrome_options.add_argument("--headless")
	chrome_options.add_argument("--window-size=1920x1080")

	#Initialize driver
	driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/Users/ryno/chromedriver")

	#Go to vk.com and get element. Print for fun/testing
	driver.get(myURL)

	#Dynamically pull page information
	counter = driver.find_element(By.CLASS_NAME, 'pv_counter').text
	counter = counter.split(' ')
	lastImgCount = counter[2]

	#Pull the image
	while True:
		wait = WebDriverWait(driver, 10)
		wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='pv_photo']/img[1]")))
		imgElement = driver.find_element(By.XPATH, "//div[@id='pv_photo']/img[1]")
		imgURL = imgElement.get_attribute('src')
		wget.download(imgURL)
		counter = driver.find_element(By.CLASS_NAME, 'pv_counter').text
		counter = counter.split(' ')
		currentImgCount = counter[0]
		print(" Current Image Count: ", currentImgCount)
		if lastImgCount == currentImgCount:
			break
		imgElement.click()

	#Timer Stops
	stop = timeit.default_timer()

	#Prints the Start and End Time to Console
	print('Time: ', stop - start)

myAnswer = input("Is this the first page? y/n \n")

if myAnswer == 'y' or myAnswer == 'Y':
	page1()
elif myAnswer == 'n' or myAnswer == 'N':
	print("More to come.....")
else:
	print("Disaster......")
