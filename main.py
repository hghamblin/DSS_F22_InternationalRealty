import pandas as pd
from scraper import Scraper

# load spreadsheet
inventory_df = pd.read_excel("Listing Inventory-19Sep2022.xlsx", header = 2)

for i, property in inventory_df.iterrows():
    
    print(f"Property {i + 1} / {len(inventory_df)}")

    # create scraper object
    scraper = Scraper(
        street = property['PROPERTY ADDRESS'], 
        city = property['CITY'], 
        state = property['STATE/\nPROVINCE'], 
        zip_code = property['ZIP/\nPOSTAL CODE'], 
        country = property['COUNTRY']
    )

    # scrape urls
    scraper.start_webdriver()
    scraper.get_urls()

    # get screenshots
    if len(scraper.urls) > 0:
        print(f"Found {len(scraper.urls)} listings for {scraper.address}")
        scraper.get_screenshots()
        scraper.create_report()
    else:
        print(f"No listings found for {scraper.address}")

    # close browser
    scraper.driver.quit()