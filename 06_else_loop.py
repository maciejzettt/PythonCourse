import os
import urllib.request as url

data_dir = "G:/py/exdata"

pages = [
    {'name': 'chemia', 'addr': 'http://chemia.amu.edu.pl/'},
    {'name': 'mobilo', 'addr': 'http://www.kursyonline24.eu'},
    {'name': 'brak', 'addr': 'http://jakis.adres.domena'}
]

for page in pages:
    path = os.path.join(data_dir, page['name']+'.html')
    try:
        url.urlretrieve(page['addr'], path)
        print(path, page['addr'], 'retrieved')
    except:
        print("An error occured.")
        break
else:
    print("No errors occured.")