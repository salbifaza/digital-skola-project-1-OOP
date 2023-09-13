from modules.book import Book
from modules.magazine import Magazine
from modules.cd import Cd
from modules.dvd import Dvd
from modules.catalog import Catalog
import json

f = open('files/data.json')
data_json = json.load(f)

list_books = []
list_magazine = []
list_cd = []
list_dvd = []

for item in data_json:
    if item['source'] == 'book':
        list_books.append(Book(
            title=item['title'],
            upc=item['upc'],
            subject=item['subject'],
            issbn=item['issbn'],
            authors=item['authors'],
            dds_number=item['dds_number']
        ))
    elif item['source'] == 'magazine':
        list_magazine.append(Magazine(
            title=item['title'],
            upc=item['upc'],
            subject=item['subject'],
            volume=item['volume'],
            issue=item['issue']
        ))
    elif item['source'] == 'cd':
        list_cd.append(Cd(
            title=item['title'],
            upc=item['upc'],
            subject=item['subject'],
            artist=item['artist']
        ))
    elif item['source'] == 'dvd':
        list_dvd.append(Dvd(
            title=item['title'],
            upc=item['upc'],
            subject=item['subject'],
            actors=item['actors'],
            directors=item['directors'],
            genre=item['genre']
        ))
    else:
        pass

catalog_all = [list_books, list_magazine, list_cd, list_dvd]

input_search = 'test'
results = Catalog(catalog_all).search(input_search)

for index, result in enumerate(results):
    print(f'result ke-{index+1} | {result}')