import requests
import os
import functools


def save_url_file(url, dir, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


msg = "Please wait - the file {} will be downloaded"

url = 'http://mobilo24.eu/spis'
dir = 'g:/py/exdata/'
file = 'spis.html'
save_url_file(url, dir, file, msg)

url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
dir = 'g:/py/exdata/'
file = 'logo.png'
save_url_file(url, dir, file, msg)

saveUrlSimple = functools.partial(save_url_file, dir="g:/py/exdata/", msg="Please wait for {}")

saveUrlSimple(url=url, file=file)

