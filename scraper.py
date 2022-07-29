from bs4 import BeautifulSoup
import requests


def get_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    list = [p.get_text() for p in soup.find_all("p", text=True)]

    total = ""
    for line in list:
        string = line.replace(u'\xa0', u' ')
        total += string + " "

    return total