from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import timeit
import wget

#Initialize x
x = 1

#Timer Starts
start = timeit.default_timer()

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()

#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

#Initialize driver
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/Users/ryno/chromedriver")

#Go to vk.com and get element. Print for fun/testing
driver.get("https://vk.com/wall-72806334_24873?z=photo-72806334_457241182%2Falbum-72806334_215256639%2Frev")
counter = driver.find_element(By.CLASS_NAME, 'pv_counter').text
counter = int(counter[5:8]) #I cheated lolol fix laterz

while (x <= counter):
    image = driver.find_element(By.XPATH, "//div[@id='pv_photo']/img[1]")
    #Downloads image
    wget.download(image.get_attribute('src')) #add out directory here
    #Move to next image
    image.click()
    x+=1
    print("\n")
    print(x)

#Timer Stops
stop = timeit.default_timer()

#Prints the Start and End Time to Console
print('Time: ', stop - start)