# basics
# other
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# search tools
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

# initialize webdriver
driver = webdriver.Chrome(
    service = Service(executable_path = ChromeDriverManager().install())
)

# load page
url = 'https://www.homes.com/'
driver.get(url)

# search bar
search_bar_xpath = "/html/body/main/section/div/div/div/div/div/div/input"
search_bar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, search_bar_xpath))
)

search_bar.click()

sleep(5)

driver.quit()