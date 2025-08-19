# import required packages
from bs4 import BeautifulSoup
import requests
import pandas as pd

# get the html from the website, including all paginations
base_url = 'https://www.scrapethissite.com/pages/forms/?page_num='

# there are 24 pages
all_pages = range(1, 25)

all_urls = [base_url + str(page) for page in all_pages]

# get the html for all 24 pages
soups = []

for url in all_urls:
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    soups.append(soup)

# Team Name
team_name = []

for soup in soups:
    names = soup.find_all('td', class_='name')
    clean_names = [name.get_text(strip=True) for name in names]
    team_name.extend(clean_names)

# Year
year = []

for soup in soups:
    years = soup.find_all('td', class_='year')
    clean_years = [season.get_text(strip=True) for season in years]
    year.extend(clean_years)

# Wins
wins = []

for soup in soups:
    victories = soup.find_all('td', class_='wins')
    clean_victories = [victory.get_text(strip=True) for victory in victories]
    wins.extend(clean_victories)

# Losses
losses = []

for soup in soups:
    defeats = soup.find_all('td', class_='losses')
    clean_defeats = [defeat.get_text(strip=True) for defeat in defeats]
    losses.extend(clean_defeats)

# OT Losses
ot_losses = []

for soup in soups:
    ot_defeats = soup.find_all('td', class_='ot-losses')
    clean_ot_defeats = [ot_defeat.get_text(strip=True) for ot_defeat in ot_defeats]
    ot_losses.extend(clean_ot_defeats)

# Win Percentage
win_percentage = []

for soup in soups:
    wps = soup.find_all('td', class_=['pct text-success', 'pct text-danger'])
    clean_wps = [wp.get_text(strip=True) for wp in wps]
    win_percentage.extend(clean_wps)

# Goals For 
goals_for = []

for soup in soups:
    gf = soup.find_all('td', class_='gf')
    clean_gf = [i.get_text(strip=True) for i in gf]
    goals_for.extend(clean_gf)

# Goals Against
goals_against = []

for soup in soups:
    ga = soup.find_all('td', class_='ga')
    clean_ga = [i.get_text(strip=True) for i in ga]
    goals_against.extend(clean_ga)

# +/-
plus_minus = []

for soup in soups:
    pm = soup.find_all('td', class_=['diff text-success', 'diff text-danger'])
    clean_pm = [i.get_text(strip=True) for i in pm]
    plus_minus.extend(clean_pm)

# create a DataFrame from the obtained lists
nhl_team_stats = pd.DataFrame({'team_name': team_name,
                               'year': year,
                               'wins': wins,
                               'losses': losses,
                               'ot_losses': ot_losses,
                               'win_percentage': win_percentage,
                               'goals_for': goals_for,
                               'goals_against': goals_against,
                               'plus_minus': plus_minus})

print(nhl_team_stats.head())
