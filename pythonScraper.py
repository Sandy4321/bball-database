import requests
import bs4

resp = requests.get('http://www.basketball-reference.com/leagues/NBA_2015_per_game.html')
soup = bs4.BeautifulSoup(resp.text)
players_table_data = soup.select("tr.full_table")
players = {}
names = [a.get_text() for a in soup.select("tr.full_table a[href^=/players]")]
for i in range(len(names)):
    players[names[i]] = players_table_data[i]
print players["Russell Westbrook"]


