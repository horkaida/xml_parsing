import requests
from bs4 import BeautifulSoup
my_xml = requests.get("https://scipost.org/atom/publications/comp-ai")
with open('my_xml.xml', 'wb') as file:
    file.write(my_xml.content)
soup = BeautifulSoup(my_xml.content, 'lxml-xml')
news = soup.find_all('entry')

def note_parsing(note):
    title = note.title.text
    link = note.link['href']
    article = requests.get(link).content
    soup_for_article = BeautifulSoup(article, 'lxml')
    article_text = soup_for_article.find('p', {'class': 'abstract'}).text
    return f"Title: {title}\nLink: {link}\nText: {article_text}\n"

for one_article in news:
    print(note_parsing(one_article))
    print("#" * 80)
