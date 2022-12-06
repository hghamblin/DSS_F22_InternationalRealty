# basics
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# search tools
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from time import sleep


# driver and profile initialization
profile_path = 'C:/Users/ee11c/AppData/Roaming/Mozilla/Firefox/Profiles/ujfo3dze.scraper-bot'
profile = FirefoxProfile(profile_path)

driver = webdriver.Firefox(
    service = Service(executable_path = GeckoDriverManager().install()),
    firefox_profile=profile
)

def landwatch_scraper(search_ad, url, curr_page, last_page):

    search_url = url + str(curr_page)

    if curr_page != 1:
        driver.get(search_url)

    # grabs listings
    linkaddy = driver.find_elements(By.CLASS_NAME, '_61961')
    element_found = False

    # main loop for searching a page for an address
    for element in linkaddy:

        # grabs and manipulates listing to be compared to the search value
        addy = element.find_element(By.CLASS_NAME, 'df867').text
        addy = addy.splitlines()
        new_ad = ''
        for i in range(len(addy)):
            new_ad += addy[i]
    
        # if address is found grab the link to the page
        if new_ad == search_ad:
            link = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
            print(link)
            element_found = True
            return

    # begins recurssion loop if address is not found on page
    if element_found == False:

        # base case for when all pages have been searched
        if curr_page == last_page:
            print('No such listing on landwatch.com')
            return

        # continues onto next page of search
        else:
            curr_page+=1
            landwatch_scraper(search_ad, url, curr_page, last_page)
     
def land_scraper(search_ad, url, curr_page, last_page):

    search_url = url + str(curr_page) + '/'

    if curr_page != 1:
        driver.get(search_url)

    # grabs listings
    linkaddy = driver.find_elements(By.CLASS_NAME, '_154c4')
    element_found = False

    # main loop for searching a page for an address
    for element in linkaddy:

        # grabs and manipulates listing to be compared to the search value
        addy = element.find_element(By.CLASS_NAME, '_61961').text
        addy = addy.splitlines()
        new_ad = ''
        for i in range(len(addy)):
            new_ad += addy[i]
    
        # if address is found grab the link to the page
        if new_ad == search_ad:
            link = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
            print(link)
            element_found = True
            return

    # begins recurssion loop if address is not found on page
    if element_found == False:

        # base case for when all pages have been searched
        if curr_page == last_page:
            print('No such listing on land.com')
            return

        # continues onto next page of search
        else:
            curr_page+=1
            land_scraper(search_ad, url, curr_page, last_page)

def land_and_farm_scraper(search_ad, url, curr_page, last_page):

    search_url = url + str(curr_page)

    if curr_page != 1:
        driver.get(search_url)

    # grabs listings
    linkaddy = driver.find_elements(By.CLASS_NAME, 'property-card--address')
    element_found = False

    # main loop for searching a page for an address
    for element in linkaddy:

        # grabs and manipulates listing to be compared to the search value
        string = element.text
        new_ad = ''
        string = string.splitlines()
        for i in range(len(string)):
            if i == 0:
                new_ad += string[i]

            if i == 1:
                new_line = ''
                string2 = string[i].split(' ,  ')
                for value in string2:
                    new_line +=', ' + value
                new_ad += new_line

            if i == 2:
                new_line = string[i]
                new_line = new_line.split(',')
                new_line = new_line[0][1:]
                new_ad += ', ' + new_line
    
        # if address is found grab the link to the page
        if new_ad == search_ad:
            link = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
            print(link)
            element_found = True
            return

    # begins recurssion loop if address is not found on page
    if element_found == False:

        # base case for when all pages have been searched
        if curr_page == last_page:
            print('No such listing on landandfarm.com')
            return

        # continues onto next page of search
        else:
            curr_page+=1
            land_and_farm_scraper(search_ad, url, curr_page, last_page)

def web_scraper(state, state_code, county, address):
    county = county.replace(' ', '-')
    state = state.replace(' ', '-')
    max_page_search = 10

    # landwatch.com scraping
    landwatch_url = f'https://landwatch.com/{state}-land-for-sale/{county}/'

    driver.get(landwatch_url)
    pages = driver.find_elements(By.CLASS_NAME, '_8cfc9')
    last_page = int(pages[len(pages)-1].text)

    search_url = landwatch_url + 'page-'

    if last_page > max_page_search:
        return
    else:
        landwatch_scraper(address, search_url, 1, last_page)

    # land.com scraping
    land_url = f'https://www.land.com/{county}-{state_code}/all-land/'

    driver.get(land_url)
    pages = driver.find_elements(By.CLASS_NAME, '_8cfc9')
    last_page = int(pages[len(pages)-1].text)

    search_url = land_url + 'page-'

    if last_page > max_page_search:
        return
    else:
        land_scraper(address, search_url, 1, last_page)

    # landandfarm.com scraping
    landandfarm_url = f'https://www.landandfarm.com/search/{state_code}/{county}-land-for-sale/?CurrentPage='

    driver.get(landandfarm_url)
    pages = driver.find_element(By.CLASS_NAME, 'big-screen-content.text-center')
    pages = pages.find_elements(By.TAG_NAME, 'a')
    length = len(pages)
    last_page = int(pages[len(pages)-1].text)

    search_url = landandfarm_url + 'page-'

    if last_page > max_page_search:
        return
    else:
        land_and_farm_scraper(address, search_url, 1, last_page)


address = ''
address2 = 'Tbd N 1800 E, Rexburg, ID, 83440, Fremont County'
web_scraper('idaho','ID','Fremont County', address)
web_scraper('idaho','ID','Fremont County', address2)


driver.quit()


