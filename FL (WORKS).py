import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# get the path of ChromeDriverServer
dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver.exe"

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(10)
# driver.maximize_window()

# Navigate to the application home page
driver.get("http://www.fallenlondon.com")

s = driver.find_element_by_xpath("//*[@id=\"emailAddress\"]")
s.send_keys("samuel.da.shadrach@gmail.com")

s = driver.find_element_by_xpath("//*[@id=\"password\"]")
s.send_keys("happybirds1")

s = driver.find_element_by_xpath("//*[@id=\"log-in\"]/form/div/button")
s.click()

while True:
    # Get actions left
    r = driver.find_element_by_xpath("//span[text()=\"Actions\"]/parent::div/div/div/span/div[1]")
    t = r.text
    print(t)
    
    if(t == "0/20"):
        break

    try:
        s = driver.find_element_by_xpath("//*[@data-branch-id=\"12795\"]/div/div[2]/div[2]/button")
        s.click()
    except NoSuchElementException:
        pass

    try:
        s = driver.find_element_by_xpath("//*[@data-branch-id=\"5375\"]/div[2]/div[3]/button")
        s.click()
    except NoSuchElementException:
        pass

    try:
        s = driver.find_element_by_xpath("//*[text()=\"Onwards\"]")
        s.click()
    except NoSuchElementException:
        pass
