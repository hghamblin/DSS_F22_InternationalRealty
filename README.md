# DSS_F21_InternationalRealty

__International Realty__
PM: Nate Duncan and Caden Franc
Tools: Python
- https://www.goldengatesir.com/eng
- https://github.com/BYUIDSS/threestory_FA21
- When real estate agents list a property for sale the property listing is shown online on the websites of up to 29 syndication partners. 
- We would like to be able to provide a PDF report that shows how the property listing appears on each of the different partner websites.
- Given a spreadsheet of active listings, return an individual PDF report for each listing in the spreadsheet where each page of the PDF displays a screenshot of the syndication partner site showing the listing.
- Each page should have text to identify the listing, the partner site, and the date the screenshot was taken.
- An alternate interaction would be to have an interface where a user could enter a property address and receive the PDF report as an output.

# threestory_FA21
Web Scraping Tool for Threestory Studio/Golden Gate Sotheby's International Realty

# Sotheby's International Realty Syndication Partner Screenshot Project

## Background
When real estate agents list a property for sale with Sotheby's International Realty, the property listing - including photos, description, property details - is shown online on the websites of up to 29 syndication partners. We would like to be able to provide a PDF report that shows how the property listing appears on each of the different partner websites.

## Desired functionality
Given a spreadsheet of active listings, return an individual PDF report for each listing in the spreadsheet where each page of the PDF displays a screenshot of the syndication partner site showing the listing. Each page should have text to identify the listing, the partner site, and the date the screenshot was taken.

An alternate interaction would be to have an interface where a user could enter a property address and receive the PDF report as an output.

Note:
Web scraping should honor robots.txt directives

## Possible Challenges
### Differing structures
There are several different structures for how the syndication partner sites organize and present the listings. For example, for some sites, it will likely be easier to search using the Property Name, and others will use the Property Address.

### Resistance to automation
Some sites throw up a Captcha challenge if they detect the site is being controlled by an automated process - these may require some user interaction.

### Resilience
The ~29 syndication partners are independent websites and periodically change the structure and presentation of the listings on their sites. That means that a script that works for a site today may not work tomorrow. How can we build resilience into the solution to accommodate those kinds of changes gracefully? Can we set up tests to quickly identify changes that might lead to scripts breaking?

## Listing Platforms
Some website syndication partners share a common platform, and use the same property identification number. If we can find the identification number on one site, we should be able to use that number as a shortcut to get to the appropriate page on another site without having to do a more complicated query. 


### Sotheby’s Listing ID Platform
The most direct examples are the sites that use the Sotheby’s International Realty Listing ID code that exists in our spreadsheet in the LISTING ID field.

For example, use 1650 Waverley Street, Palo Alto, CA, which has a LISTING ID of **M4V5P6**

_Shortcut URLs:_  
Sotheby's International Realty: <https://www.sothebysrealty.com/id/M4V5P6>  
Golden Gate Sotheby's International Realty: <https://www.goldengatesir.com/id/M4V5P6>  
James Edition: <https://www.jamesedition.com/ref/M4V5P6>  
Juwai: <https://www.juwai.com/find-listing-by-source?source=Sothebys&source_id=M4V5P6>  
Real-Buzz: <http://real-buzz.com/RealEstate-detail-SIR/M4V5P6>  
Country Life: <http://countrylife.co.uk/international-property/M4V5P6>

### James Edition Platform
Note that the James Edition shortcut link above forwards to this URL:
<https://www.jamesedition.com/real_estate/palo-alto-ca-usa/rarely-available-old-palo-alto-property-of-distinction-12039664>

If you extract the numbers at the end of the URL, we can use that ID number to go directly to the correct results pages of one other website:

_Shortcut URL:_  
Expansion: <https://expansion.mx/inmobiliario/propiedades/12039664>  

### PropGoLuxury Platform
For this one, you would have to do a normal query initially to get the right code, then extract.

The full length URL:
<https://www.propgoluxury.com/en/homes/4372526/palo-alto-property-for-sale/rarely-available-old-palo-alto-property-of-distinction>

_Shortcut URLs:_  
PropGoLuxury: <https://www.propgoluxury.com/en/homes/4372526>  
Financial Times: <https://propertylistings.ft.com/homes/4372526>  
Nikkei: <https://propertylistings.nikkei.jp/jp/homes/4372526>

### Mansion Global Platform
For this one, you would have to do a normal query initially to get the right code, then extract.

The full length URL:  
<https://www.mansionglobal.com/listings/6035537-1650-waverley-street-94301?mod=mg_search_united-states_california_palo-alto&pos=6&page=1>

_Shortcut URLs:_  
WSJ: <https://realestate.wsj.com/listings/6035537>  
Manion Global: <https://www.mansionglobal.com/listings/6035537>  
Market Watch: <https://www.marketwatch.com/personal-finance/real-estate/listings/6035537>  
Barrons: <https://www.barrons.com/real-estate/listings/6035537>

### Luxury Estate Platform
Discover common code:  
Luxury Estate: https://www.luxuryestate.com/p127727721-detached-house-for-sale-palo-alto  

**Shortcut URLs:**  
Luxury Estate: <https://www.luxuryestate.com/p127727721-detached-house-for-sale-palo-alto>  
House24: <http://www.house24.ilsole24ore.com/p127727721-casa-unifamiliare-in-vendita-palo-alto>

### Land.com Platform
These three sites are supposedly all powered by the same land.com platform, but I haven't seen any common threads.
https://www.land.com/property/24021-Highway-9-Los-Gatos-California-95033/10853543/

Lands of America: <https://www.landsofamerica.com/property/15400-Madrone-Hill-Road-Saratoga-California-95070/10063810/>  
LandWatch: <https://www.landwatch.com/santa-cruz-county-california-land-for-sale/pid/410260025>  
Land and Farm: <https://www.landandfarm.com/property/644_Acres_in_Santa_Cruz_County-13353857/>

### ListGlobally Platform

https://www.properstar.com/listing/80938647
https://international.99acres.com/listing/80938647

### Unconnected Platforms
That leaves the rest of these that need to be queried individually:  
Homes.com: <https://www.homes.com/property/1650-waverley-st-palo-alto-ca/e167m3mms612x/> 
Le Figaro: <https://properties.lefigaro.com/announces/house-santa+clara-california-united+states/45044836/>

Realtor.com: <https://www.realtor.com/realestateandhomes-detail/1650-Waverley-St_Palo-Alto_CA_94301_M23834-67979>  

**Nextdoor**  
Nextdoor requires a local user account, so I'm not hopeful that we can effectively screenshot listings on this site.  
https://nextdoor.com/real-estate-listings/30513705

## History
A previous developer wrote a series of Python scripts that were mostly successful in capturing screenshots from a number of the sites. Those files are included in the repository for reference and can be used and modified. 

## Reference files
* Google doc showing details of all syndication partners, including rules for listings to appear: <https://docs.google.com/spreadsheets/d/1QBtn4Po3W3h0e7TYwelWYDTdErFvjxl0VOkwlU9sH6M/edit#gid=0>
* Previously written Python code and supporting files (in legacy_code directory)
* Excel file of current listing data (Listing Inventory-19Sep2022.xlsx)
* Sample of desired PDF output (screenshot-pdf-template.pdf)
Austin
