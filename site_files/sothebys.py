# basics
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options # to be used later (--headless)
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from webdriver_manager.firefox import GeckoDriverManager

# search tools
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

# FOR TESTING ONLY
address = "Romazzino Porto Cervo, Sassari, Italy"

# load profile
profile_path = 'profile/'
profile = FirefoxProfile(profile_path)

# initialize webdriver
driver = webdriver.Firefox(
    service = Service(executable_path = GeckoDriverManager().install()), 
    firefox_profile = profile
)

# load page
url = 'https://www.sothebysrealty.com/eng'
driver.get(url)

# search address
search_bar_xpath = "/html/body/div/div/div/main/section[1]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/input"
search_bar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, search_bar_xpath))
)
search_bar.send_keys(address + Keys.ENTER)

sleep(3)

# get property ID
id_xpath = "/html/body/div[1]/div/div/main/div[1]/section[4]/div/div[1]/ul/li[1]/ul/li[1]/div[2]"
property_id = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, id_xpath))
).text

sleep(3)

print(f"https://www.sothebysrealty.com/id/{property_id}")
print(f"https://www.goldengatesir.com/id/{property_id}")
print(f"https://www.jamesedition.com/ref/{property_id}")
print(f"https://www.juwai.com/find-listing-by-source?source=Sothebys&source_id={property_id}")
print(f"http://www.real-buzz.com/RealEstate-detail-SIR/{property_id}")
print(f"http://www.countrylife.co.uk/international-property/{property_id}")

driver.quit()