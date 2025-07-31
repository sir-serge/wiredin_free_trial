import requests
from bs4 import BeautifulSoup

url = 'https://bbc.com/news/world/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

titles = soup.find_all('h2', class_='sc-4fedabc7-3')

print(titles)