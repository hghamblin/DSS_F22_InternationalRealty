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
address = "144 Huckleberry Trail, Woodside, CA 94062"

# load profile
profile_path = '../profile/'
profile = FirefoxProfile(profile_path)

# initialize webdriver
driver = webdriver.Firefox(
    service = Service(executable_path = GeckoDriverManager().install()), 
    firefox_profile = profile
)

# load page
url = f'https://www.mansionglobal.com/'
driver.get(url)

# search address
search_bar_xpath = "/html/body/div[1]/div/div/div/header/div[2]/div[2]/div/form/div/div/div/div[1]/div/div[2]/input"
search_bar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, search_bar_xpath))
)
search_bar.send_keys(address)

# click top result
result_xpath = "/html/body/div[1]/div/div/div/header/div[2]/div[2]/div/form/div/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/button"
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, result_xpath))
).click()

# load listing
WebDriverWait(driver, 10).until(
    EC.url_changes(url)
)

# extract id from listing url
listing_url = driver.current_url
id = listing_url.split('/')[-1]

# print links
print(f"https://www.mansionglobal.com/listings/{id}")
print(f"https://realestate.wsj.com/listings/{id}")
print(f"https://www.marketwatch.com/personal-finance/real-estate/listings/{id}")
print(f"https://www.barrons.com/real-estate/listings/{id}")

driver.quit()