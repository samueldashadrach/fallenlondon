# import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# get the path of ChromeDriverServer
# dir = os.path.dirname(__file__)
# chrome_driver_path = dir + "\chromedriver.exe"

# create a new Chrome session
# driver = webdriver.Chrome(chrome_driver_path)

desired_cap = {
 'browser': 'Chrome',
 'browser_version': '70.0',
 'os': 'Windows',
 'os_version': '10',
 'resolution': '1024x768'
}

driver = webdriver.Remote(
    command_executor='http://samuelshadrach1:YkZ6h4pGioDVAFTm5oZy@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)

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
    
driver.quit()
