# general
import pandas as pd

# web tools
from flask import Flask, request, redirect, url_for, render_template

# scraper class
from scraper import Scraper

# initialize app
app = Flask(__name__)

# home page
@app.route('/')
def home():
    return render_template('index.html')

def scrape_address(street, city, state, zip_code, country, price):

    # create scraper object
    scraper = Scraper(street, city, state, zip_code, country, price)

    # scrape website
    scraper.start_webdriver()
    scraper.get_urls()
    scraper.get_screenshots()

    # create report
    scraper.create_report()

    # close browser
    scraper.driver.quit()

@app.route('/spreadsheet', methods = ["POST"])
def scrape_from_excel():

    # upload file
    upload = request.files['excel_file']
    upload.save(upload.filename)

    # load dataframe
    inventory_df = pd.read_excel(upload.filename, header = 2)

    # scrape addresses
    for _, property in inventory_df.iterrows():
        scrape_address(
            property['PROPERTY ADDRESS'], 
            property['CITY'], 
            property['STATE/\nPROVINCE'], 
            property['ZIP/\nPOSTAL CODE'], 
            property['COUNTRY'], 
            0
        )

    return redirect(url_for('home'))

@app.route('/user_input', methods = ["POST"])
def scrape_from_input():
    
    # get inputs
    street = request.form['street']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip-code']
    country = request.form['country']
    price = request.form['price'].replace('$', '').replace(',', '')

    # # scrape address
    scrape_address(street, city, state, zip_code, country, price)

    return redirect(url_for('home'))

if __name__ == '__main__':
 
    app.run(debug = True)