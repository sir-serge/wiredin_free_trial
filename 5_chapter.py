import requests
from bs4 import BeautifulSoup

url = 'https://bbc.com/news/world/'

response = requests.get(url)

#  Pass the HTML content, not the response object
soup = BeautifulSoup(response.text, 'lxml')

# Find all h3 tags with the specified class
h2 = soup.find_all('li', class_='sc-1bad1f0d-2')

# print(f"{h2} h3 text")
# # print(soup.prettify())

heading=title.getText()
