import requests
import bs4

resp = requests.get('http://www.basketball-reference.com/leagues/NBA_2015_per_minute.html?lid=header_seasons')
soup = bs4.BeautifulSoup(resp.text)
players_table_data = soup.select("tr.full_table")
pos = ['PG', 'SG', 'SF', 'PF', 'C']


#retrieves list of player names from html table
def get_names():
    names = [a.get_text() for a in soup.select("tr.full_table a[href^=/players]")]
    return names

#making dictionary matching player names to stats/info
def get_dict(names):
    players = {}
    for i in range(len(names)):
        players[names[i]] = players_table_data[i].text.strip().split()
        #For long names
        if len(players[names[i]]) > 31 or players[names[i]][3] not in pos:
            l = players[names[i]]
            if l[4] in pos:
                g = l[0:2]
                g[1] = l[1] + ' ' + l[2]
                rest = l[3:]
                g.extend(rest)
                players[names[i]] = g
            if l[5] in pos:
                g = l[0:3]
                g[2] = l[2] + ' ' + l[3] + ' ' + l[4]
                rest = l[5:]
                g.extend(rest)
                players[names[i]] = g

        if "'" in players[names[i]][1]:
            n = players[names[i]][1]
            n = n.replace("'", "''")
            players[names[i]][1] = n

        if "'" in players[names[i]][2]:
            n = players[names[i]][2]
            n = n.replace("'", "''")
            players[names[i]][2] = n

        # if "'" in players[names[i]][1]:
        #For invalid FG percentages
        if players[names[i]][9] == '0.0' and players[names[i]][10] == '0.0' and len(players[names[i]]) < 30:
            l = players[names[i]]
            g = l[0:11]
            rest = l[11:]
            g.append(.000)
            g.extend(rest)
            players[names[i]] = g
        #For invalid 3PT percentages   
        if players[names[i]][12] == '0.0' and players[names[i]][13] == '0.0' and len(players[names[i]]) < 30:
            l = players[names[i]]
            g = l[0:14]
            rest = l[14:]
            g.append(.000)
            g.extend(rest)
            players[names[i]] = g
        #For invalid 2PT percentages
        if players[names[i]][15] == '0.0' and players[names[i]][16] == '0.0' and len(players[names[i]]) < 30:
            l = players[names[i]]
            g = l[0:17]
            rest = l[17:]
            g.append(.000)
            g.extend(rest)
            players[names[i]] = g
        # #For invalid eFG percentages
        # if players[names[i]][9] == '0.0' and players[names[i]][10] == '0.0' and len(players[names[i]]) < 31:
        #     l = players[names[i]]
        #     g = l[0:18]
        #     rest = l[18:]
        #     g.append(.000)
        #     g.extend(rest)
        #     players[names[i]] = g
        #For invalid FT percentages
        if players[names[i]][18] == '0.0' and players[names[i]][19] == '0.0' and len(players[names[i]]) < 30:
            l = players[names[i]]
            g = l[0:20]
            rest = l[20:]
            g.append(0.000)
            g.extend(rest)
            players[names[i]] = g
    return players