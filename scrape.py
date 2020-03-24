# requests performs a HTML request to the given website.
import requests
# beautifulSoup allows us to parse HTML
from bs4 import BeautifulSoup

# Use requests to get the HTML content of the webpage
URL = "https://en.cppreference.com/w/"
page = requests.get(URL)

# Use BS to parse the HTML content of the webpage
soup = BeautifulSoup(page.content, 'html.parser')
# use the soup.find function to filter out certain elements of the HTML
results = soup.find(title='cpp/string')

# results.prettify() formats the html nicely
print(results.prettify())

# results.text returns the text content of the HTML element.
print(results.text)