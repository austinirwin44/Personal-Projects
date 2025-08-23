# import required packages
from bs4 import BeautifulSoup
import requests
import pandas as pd

# obtain the html from the website
html_text = requests.get('https://www.scrapethissite.com/pages/simple/').text

soup = BeautifulSoup(html_text, 'lxml')

# Name
country_name_html = soup.find_all('h3', class_='country-name')
country_name = [name.get_text(strip=True) for name in country_name_html]

# Capital
country_capital_html = soup.find_all('span', class_='country-capital')
country_capital = [capital.get_text(strip=True) for capital in country_capital_html]

# Population 
country_pop_html = soup.find_all('span', class_='country-population')
country_pop = [pop.get_text(strip=True) for pop in country_pop_html]

# Area
country_area_kmsq_html = soup.find_all('span', class_='country-area')
country_area_kmsq = [area.get_text(strip=True) for area in country_area_kmsq_html]

# create a DataFrame from the obtained lists
countries = pd.DataFrame({'Name' : country_name,
                          'Capital' : country_capital,
                          'Population' : country_pop,
                          'Area (km^2)' : country_area_kmsq},
                          columns=['Name', 'Capital', 'Population', 'Area (km^2)'])

# inspect the resulting DataFrame
print(countries.head())