from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
now = datetime.now()

url2 = "https://basketball.realgm.com/gleague/teams(/_______/___)/schedule"
result2 = requests.get(url2)
  
schedule = BeautifulSoup(result2.text, "html.parser")

def upcoming():
    tbl_elements = schedule.find_all('table', class_='basketball compact dms_colors')
    # Select second table on webpage, limit find to tbody
    game = tbl_elements[1]
    tbody = game.find('tbody')
    # Find all tr elements within the table
    rows = tbody.find_all('tr')
      
    # Initialize an empty list to hold the entries
    entries = []
    
    # Iterate through the tr elements
    for row in rows:
        # Find the td elements within the tr element
        date_td = row.find('td', {'data-th': 'Date'})
        opponent_td = row.find('td', {'data-th': 'Opponent'})
    
        # Find all br elements within the td element
        br_tags = date_td.find('br')
    
        # Get the date string from the previous sibling of the br tag
        date_str = br_tags.previous_sibling
        time_str = br_tags.next_sibling
      
        # Get the text content of the td elements
        opponent_text = opponent_td.text if opponent_td else ''
    
        # Parse the date string into a datetime object
        game_date = datetime.strptime(date_str, "%b %d, %Y")
        
        # Only include games that are on or after the current date
        if game_date >= now:
            # Create a new entry for the list widget
            entry = "###### **Delaware " + opponent_text + "**" + "\n"  
            entry += "###### " + date_str + " @ " + time_str + "\n" + "---" + "\n"
            # Add the entry to the list of entries
            entries.append(entry)
        
        # Stop after 5 games added to entries
        if len(entries) >= 5:
            break
    
    # Concatenate the entries into a single string
    text = "".join(entries)
    return text