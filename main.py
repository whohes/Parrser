from bs4 import BeautifulSoup
import urllib.request

def parse():
    url = 'https://omgtu.ru/general_information/the-structure/the-department-of-university.php'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")

    block = soup.findAll('div', class_='main__content')
    description = ''

    f = open('text.txt', 'w', encoding='utf-8')

    for data in block:
        if data.find('a'):
            description = data.text

            f.write(description)

    print(description)

parse()