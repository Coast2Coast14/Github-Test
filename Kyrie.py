import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from app import *

test = get_page('https://www.basketball-reference.com/players/r/russebi01.html')

x = np.arange(19, 30)
fig, ax = plt.subplots()
colors = {'CLE': 'maroon', 'BOS': 'tab:green', 'BRK': 'k'}
plt.bar(df['Age'], df['PTS'], color=df['Tm'].map(colors))
plt.title('Kyrie Irving Points per Game by Age')
plt.xlabel('Age')
plt.xticks(x)
plt.ylabel('Points per Game')
plt.ylim([18, 28])
ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.show()

df2 = df[['Age', 'PTS']].copy()

test_size = 9

train, test = df2.iloc[:test_size], df2.iloc[test_size:]

fig, ax = plt.subplots(1, 1, figsize=(10, 5))
ax.plot(train['Age'], train['PTS'])
ax.plot(test['Age'], test['PTS'])
plt.show()


if __name__ == "__main__":
    main()
