from bs4 import BeautifulSoup
import requests

# Scrape url for roster and schedule
url = "https://www.espn.com/nba-g-league/standings"
result = requests.get(url)

# BeautifulSoup to parse HTML  
soup = BeautifulSoup(result.text, "html.parser")

def standings():

  # Eastern Conference Standings
  tr_elements = soup.find("tbody")
  
  # Create the initial table layout
  table = "| Team | W | L | GB |"
  table += "\n|---|---|---|:---:|" + "\n| "

  td_elements = soup.find_all('span', class_='stat-cell')
  wins = td_elements[0:180:12]
  losses = td_elements[1:181:12]
  gbs = td_elements[3:183:12]
  
  for tr, win, loss, gb in zip(tr_elements, wins, losses, gbs):
      teams = tr.find("td", class_="Table__TD").text
      team = teams[3:]
      win_text = str(win.text)
      loss_text = str(loss.text)
      gb_text = str(gb.text)
      table += team + " | " + win_text + " | " + loss_text + " | " + gb_text + " | " + " \n "
  return table