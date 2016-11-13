from bs4 import BeautifulSoup
import urllib2

wiki = "https://en.wikipedia.org/wiki/List_of_airports_in_the_United_States"
header = {'User-Agent': 'Mozilla/5.0'}  # Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki, headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page, "html.parser")

IATA = ""
state_of_airports = {}

table = soup.find("table", {"class": "wikitable"})

for row in table.findAll("tr"):
    cells = row.findAll("td")
    if len(cells) == 7:
        if cells[2].find(text=True) != None:
            IATA = cells[2].find(text=True)
            state_of_airports[IATA] = str(state)
    elif len(cells) != 0:
        state = cells[0].find(text=True)
        print(state)


print(state_of_airports)

