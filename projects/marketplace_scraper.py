from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as soup
import pandas as pd
import re
import time

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Set up base URL
base_url = "https://www.facebook.com/marketplace/nyc/search/?"
# Set up search parameters
min_price = 1500
max_price = 6000
days_listed = 60
min_mileage = 25000
max_mileage = 185000
min_year = 1998
max_year = 2015
transmission = ""
make = "Honda"
model = ""

# Set up full URL
url = f"{base_url}minPrice={min_price}&maxPrice={max_price}&daysSinceListed={days_listed}&maxMileage={max_mileage}&maxYear={max_year}&minMileage={min_mileage}&minYear={min_year}&transmissionType={transmission}&query={make}{model}&exact=false"

# Visit the website
driver.get(url)

# Close the popup if present
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Close"]'))
    ).click()
except:
    pass

# Scroll down to load more results
scroll_count = 10
scroll_delay = 2
for _ in range(scroll_count):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_delay)

# Parse the HTML using BeautifulSoup from the updated page source
market_soup = soup(driver.page_source, 'html.parser')

# Initialize lists to store data
names = []
prices = []
locations = []
mileages = []
urls = []

# Extract information from each listing
listings = market_soup.find_all('div', class_='x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x1e558r4 x150jy0e x1iorvi4 xjkvuk6 xnpuxes x291uyu x1uepa24')

for listing in listings:
    # Extract price
    price_element = listing.find('span', class_='x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x3x7a5m x1lkfr7t x1lbecb7 x1s688f xzsf02u')
    price = price_element.text.strip() if price_element else "N/A"
    prices.append(price)

    # Extract name
    name_element = listing.find('span', class_='x1lliihq x6ikm8r x10wlt62 x1n2onr6')
    name = name_element.text.strip() if name_element else "N/A"
    names.append(name)

    # Extract location and mileage
    info_elements = listing.find_all('span', class_='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft')
    location = "N/A"
    mileage = "N/A"

    for info_element in info_elements:
        text = info_element.get_text(strip=True)
        if re.match(r'^[a-zA-Z,\s]+$', text):  # Match location
            location = text
        elif re.match(r'^\d+\s?[Kk]?\s?miles?$', text):  # Match mileage
            mileage = text

    locations.append(location)
    mileages.append(mileage)

    # Extract URL using BeautifulSoup
    url_element = listing.find('a', href=True)
    url = url_element['href'] if url_element else "N/A"
    if url != "N/A" and not url.startswith("https"):
        url = 'https://www.facebook.com' + url
    urls.append(url)

# Create DataFrame from the lists
data = {
    'Name': names,
    'Price': prices,
    'Location': locations,
    'Mileage': mileages,
    'URL': urls
}
df = pd.DataFrame(data)

# Filter out rows where Name is "N/A"
df_filtered = df[df['Name'] != 'N/A']

# Output DataFrame to CSV
csv_filename = f'{make}{model}_marketplace_listings.csv'
df_filtered.to_csv(csv_filename, index=False)

# Quit the webdriver
driver.quit()
