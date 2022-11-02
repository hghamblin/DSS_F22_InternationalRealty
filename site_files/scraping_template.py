# basics
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from webdriver_manager.firefox import GeckoDriverManager

# search tools
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# FOR TESTING ONLY
address = "1650 Waverley Street, Palo Alto, California, 94301 United States"

# load profile
profile_path = '../profile/'
profile = FirefoxProfile(profile_path)

# initialize webdriver
driver = webdriver.Firefox(
    service = Service(executable_path = GeckoDriverManager().install()), 
    firefox_profile = profile
)

# load page
url = ''
driver.get(url)

# search address

# print url

driver.quit()