from bs4 import BeautifulSoup
import requests

# Scrape url for roster
url = "https://basketball.realgm.com/gleague/teams/(______)"
result = requests.get(url)

# BeautifulSoup to parse HTML
soup = BeautifulSoup(result.text, "html.parser")

def roster():
    # Create the initial table layout
    table = "| # | Name | Position |"
    table += "\n|--------|:------------:|:--------:|"

    tr_elements = soup.select("tr", limit=14)

    # Loop through each tr element
    for tr in tr_elements:

      # Extract the text from each td element in the tr element
        tds = [td.text for td in tr.find_all("td")]

        if len(tds) == 0 or len(tds) < 3:
          # Skip this element if the list is empty
          continue
          # Check if the tr element has the "purple" class
        if tr.has_attr('class') and 'purple' in tr['class']:
        # Add the "(*)" string after "str(tds[1])"
          tds[1] += " (*)"

        # Add a new row with the values of tds[0], tds[1], and tds[2]
        table += "\n| " + str(tds[0]) + " | " + str(tds[1]) + " | " + str(tds[2]) + " |"
    return table

