from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import timeit
import wget

def page1(myDriver, myFolder):
	myURL = input("Please enter the link and press ENTER. \n")
	#Timer Starts
	start = timeit.default_timer()

	# instantiate a chrome options object so you can set the size and headless preference
	chrome_options = Options()

	#chrome_options.add_argument("--headless")
	chrome_options.add_argument("--window-size=1920x1080")

	#Initialize driver
	driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=myDriver)


	#Go to vk.com and get element. Print for fun/testing
	driver.get(myURL)
	
	#Dynamically pull page information
	wait = WebDriverWait(driver, 30)
	try:
		wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'pv_counter')))
	except:
		print("It could not find the picture are you on vk.com?")
		return 1
	counter = driver.find_element(By.CLASS_NAME, 'pv_counter').text
	counter = counter.split(' ')
	lastImgCount = counter[2]

	#Pull the image
	while True:
		wait = WebDriverWait(driver, 30)
		try:
			wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='pv_photo']/img[1]")))
		except:
			print("It could not find the picture are you on vk.com?")
			return 1
		imgElement = driver.find_element(By.XPATH, "//div[@id='pv_photo']/img[1]")
		imgURL = imgElement.get_attribute('src')
		wget.download(imgURL, out=myFolder)
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

def main():
	tk.Tk().withdraw()
	myDriver = askopenfilename()
	myFolder = askdirectory()
	myAnswer = input("Is this the first page? y/n \n")

	if myAnswer == 'y' or myAnswer == 'Y':
		page1(myDriver,myFolder)
		#myReturn = page1(myDriver, myFolder)
		#return myReturn
	elif myAnswer == 'n' or myAnswer == 'N':
		print("More to come.....")
	else:
		print("Disaster......")


if __name__ == "__main__":
	main()
	#myReturn2 = main()
	#print("myReturn: ", myReturn2)