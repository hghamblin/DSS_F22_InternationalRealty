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

from time import sleep

WAIT_TIME = 5

city = 'LOS GATOS'
state = 'CALIFORNIA'

# load profile
profile_path = 'C:/Users/hgham/AppData/Roaming/Mozilla/Firefox/Profiles/h0i4z63s.web-scraper'
profile = FirefoxProfile(profile_path)

# configure options
options = Options()
# options.add_argument('--headless')

# configure webdriver
driver = webdriver.Firefox(
    service = Service(executable_path = GeckoDriverManager().install()), 
    firefox_profile = profile, 
    options = options
)
        
url = "https://www.landwatch.com/"
driver.get(url)

search_bar_xpath = "/html/body/div/div[2]/div/section[1]/section/div/div/div/div/div/div/div/div"
search_bar = WebDriverWait(driver, WAIT_TIME).until(
    EC.presence_of_element_located((By.XPATH, search_bar_xpath))
)
search_bar.click()

search_input_xpath = "/html/body/div/div[2]/div/section[1]/section/div/div/div/div/div/div/div/div[1]/div/div/input"
search_input = WebDriverWait(driver, WAIT_TIME).until(
    EC.presence_of_element_located((By.XPATH, search_input_xpath))
)
search_input.send_keys(f"{city}, {state}")

suggestion_xpath = "/html/body/div/div[2]/div/section[1]/section/div/div/div/div/div/div/div/div[2]/div/div/button"
suggestion = WebDriverWait(driver, WAIT_TIME).until(
    EC.presence_of_element_located((By.XPATH, suggestion_xpath))
)
suggestion.click()

# # grabs listings
# linkaddy = WebDriverWait(driver, WAIT_TIME).until(
#     EC.presence_of_all_elements_located((By.CLASS_NAME, '_61961'))
# )

# # main loop for searching a page for an address
# for element in linkaddy:

#     # grabs and manipulates listing to be compared to the search value
#     addy = element.find_element(By.CLASS_NAME, 'df867').text
#     addy = addy.splitlines()
#     new_ad = ''
#     for i in range(len(addy)):
#         new_ad += addy[i]

#     # if address is found grab the link to the page
#     if new_ad == self.address:
#         link = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
#         print(link)
#         element_found = True
#         return

# # begins recurssion loop if address is not found on page
# if element_found == False:

#     # how to grab the next url if its the first page
#     if iterator == 1:
#         iterator+=1
#         element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[3]/div/div[2]/div[4]/a')
#         link = element.get_attribute('href')
#         page_scraper(search_ad, link, iterator)

#     # how to grab the next page if its not the first page
#     else:
#         element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[3]/div/div[2]/div[3]/a[2]')
#         link = element.get_attribute('href')
#         page_scraper(search_ad, link, iterator)