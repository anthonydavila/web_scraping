#web scraping con beautiful soup

#importar las librerias
import requests
import html5lib
from bs4 import BeautifulSoup




response = requests.get("https://www.google.com")

soup = BeautifulSoup(response.content, "html5lib")
print(soup.prettify())