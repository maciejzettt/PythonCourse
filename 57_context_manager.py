import os
import requests as rq
import zipfile as zip


class FileFromWeb:
    def __init__(self, url, tmpfile):
        self.url = url
        self.tmpfile = tmpfile

    def __enter__(self):
        self.response = rq.get(self.url)
        with open(self.tmpfile, 'bw') as f:
            f.write(self.response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.tmpfile)


with FileFromWeb("https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip", "h:/temp/euroxref.zip") as file:
    with zip.ZipFile(file.tmpfile, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir("h:/temp/")
        z.extract(a_file, '.', None)
