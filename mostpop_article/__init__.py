import requests
from bs4 import BeautifulSoup


def data_extraction():
    try:
        content = requests.get('https://www.detik.com/')
    except Exception():
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        webResult = soup.find(
            'div', {'class': 'box cb-mostpop'})
        webResult = webResult.findChildren(
            'a', {'class': 'media__link'}, href=True)

        i = 0
        for res in webResult:
            title = res.text
            link = res['href']
            print(f"Judul: {title}")
            print(f"Link: {link}\n")
            i = i + 1
