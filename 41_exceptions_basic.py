import requests
import os
import shutil


def save_url_to_file(cUrl, cFile_path):
    r = requests.get(cUrl, stream=True)
    with open(cFile_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = 'g:/py/exdata/'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.isfile(tmpfile_path):
        os.remove(tmpfile_path)
    save_url_to_file(url, tmpfile_path)
    shutil.copy(tmpfile_path, file_path)
except Exception as e:
    print("An error has occured: {0}".format(e))
else:
    print("File downloaded successfully.")
finally:
    if os.path.isfile(tmpfile_path):
        os.remove(tmpfile_path)