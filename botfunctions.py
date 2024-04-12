import sqlite3
from bs4 import BeautifulSoup
import requests



# Function for scraping webpage
def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.text
        paragraphs = [p.text for p in soup.find_all('p')]
        return title, '\n'.join(paragraphs)
    else:
        print("Failed to retrieve webpage: ", response.status_code)
        return None, None

# Function to create database and populate it with webpage info
def create_database():
    conn = sqlite3.connect('webpages.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS webpages (url TEXT PRIMARY KEY, title TEXT, content TEXT)''')
    conn.commit()

    # URLs
    urls = ['https://www.imdi.no/en/', 
    'https://www.imdi.no/en/english-pages/fast-and-accurate-settlement-work/']

    for url in urls:
        title, content = scrape_page(url)
        if title and content:
            c.execute("INSERT INTO webpages VALUES (?, ?, ?)", (url, title, content))

    conn.commit()
    conn.close()