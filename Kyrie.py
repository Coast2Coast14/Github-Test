import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Sets the URL I'm retrieving the data from
URL = 'https://www.basketball-reference.com/players/i/irvinky01.html'

# Imports the URL
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'lxml')

# Creates an empty dataframe
columns = ['Age', 'Tm', 'Lg', 'Pos', 'G', 'GS', 'MP', 'FG', 'FGA',
           'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT',
           'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK',
           'TOV', 'PF', 'PTS']
df = pd.DataFrame(columns=columns)

table = soup.find('table', attrs={'id': 'per_game'}).tbody
trs = table.find_all('tr')
print(table)
# imports data into dataframe
for tr in trs:
    tds = tr.find_all('td')
    row = [td.text.replace('\n', '') for td in tds]
    df = df.append(pd.Series(row, index=columns), ignore_index=True)

# plots the data
plt.plot(df[['Age']], df[['PTS']], xlabel='Age', ylabel='Points per Game')
plt.title('Kyrie Irving Points per Game by Age')
plt.show()


def main():
    pass


if __name__ == "__main__":
    main()
