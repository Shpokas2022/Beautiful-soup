from bs4 import BeautifulSoup
import requests
google = requests.get('https://google.com')
google.content
google.status_code