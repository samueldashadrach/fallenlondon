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
    command_executor='INSERT_EXECUTOR_HERE',
    desired_capabilities=desired_cap)

driver.implicitly_wait(10)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://www.fallenlondon.com")

s = driver.find_element_by_xpath("//*[@id=\"emailAddress\"]")
s.send_keys("INSERT_USERNAME_HERE")

s = driver.find_element_by_xpath("//*[@id=\"password\"]")
s.send_keys("INSERT_PASSWORD_HERE")

s = driver.find_element_by_xpath("//*[@id=\"log-in\"]/form/div/button")
s.click()

# Close Holiday Special window (The Price of Loss)
try:
    s = driver.find_element_by_xpath("//*[@class=\"fa fa-inverse fa-stack-1x fa-close\"]")
    s.click()
except NoSuchElementException:
    pass

while True:
    # Get actions left
    r = driver.find_element_by_xpath("//span[text()=\"Actions\"]/parent::div/div/div/span/div[1]")
    t = r.text
    print(t)
    
    if(t == "0/20"):
        break
        
    # Main storyline
    try:
        s = driver.find_element_by_xpath("//*[@data-branch-id=\"10375\"]/div/div[2]/div[2]/button") # The alleys of spite
        s.click()
    except NoSuchElementException:
        pass

    # Storylet option
    try:
        s = driver.find_element_by_xpath("//*[@data-branch-id=\"39444\"]/div[2]/div[2]/button") # The cats of Spite
        s.click()
    except NoSuchElementException:
        pass

    try:
        s = driver.find_element_by_xpath("//*[text()=\"Onwards\"]")
        s.click()
    except NoSuchElementException:
        pass

    try:
        s = driver.find_element_by_xpath("//*[@data-branch-id=\"4489\"]/div[2]/div[3]/button") # The cats of Spite
        s.click()
    except NoSuchElementException:
        pass

    
driver.quit()
