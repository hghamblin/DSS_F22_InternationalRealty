# basics
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# search tools
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# other
from time import sleep


# configure webdriver
driver = webdriver.Firefox(
    service = Service(executable_path = GeckoDriverManager().install())
)

# load page
url = "https://www.land.com/"
driver.get(url)

sleep(5)

# close browser
driver.quit()