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
from selenium.webdriver.support.ui import Select

# FOR TESTING ONLY
street_address = "144 Huckleberry Trail"
city = "Woodside"
state = "California"
country = "United States"

# load profile
profile_path = '../profile/'
profile = FirefoxProfile(profile_path)

# initialize webdriver
driver = webdriver.Firefox(
    service = Service(executable_path = GeckoDriverManager().install()), 
    firefox_profile = profile
)

# load page
url = f'https://www.propgoluxury.com/'
driver.get(url)

# search country
country_bar_xpath = "/html/body/div[1]/div[3]/div/div[2]/form/div/table/tbody/tr[1]/td/span/select"
country_bar = Select(WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, country_bar_xpath))
))
country_bar.select_by_visible_text(country)

# search state
state_xpath = "/html/body/div[1]/div[3]/div/div[2]/form/div/table/tbody/tr[2]/td/span/select"
state_bar = Select(WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, state_xpath))
))
state_bar.select_by_visible_text(state)

# search city
city_xpath = "/html/body/div[1]/div[3]/div/div[2]/form/div/table/tbody/tr[3]/td/span/span/input"
city_bar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, city_xpath))
)
city_bar.send_keys(city + Keys.ENTER)

# submit
submit_xpath = "/html/body/div[1]/div[3]/div/div[2]/form/div/table/tbody/tr[5]/td/div[2]/input"
driver.find_element(By.XPATH, submit_xpath).click()

# get results
listings = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "ai-search-result"))
)

# find correct listing
listing_urls = [listing.find_element(By.TAG_NAME, 'a').get_attribute('href') for listing in listings]
for url in listing_urls:

    # load listing
    driver.get(url)

    # get address
    address_xpath = "/html/body/div[1]/div[3]/div[2]/div[4]/div[1]/div[2]/h3/span"
    listing_address = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, address_xpath))
    ).text
    
    # check if address matches
    if street_address.lower() == listing_address.lower()[:-1]:
        id = driver.current_url.split('/')[5]
        print(id)
        break

# print links
print(f"https://www.propgoluxury.com/en/homes/{id}")
print(f"https://propertylistings.ft.com/homes/{id}")
print(f"https://propertylistings.nikkei.jp/jp/homes/{id}")

driver.quit()