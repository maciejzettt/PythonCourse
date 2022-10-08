import os
import requests


def gen_get_files(dir):
    try:
        result_list = os.listdir(dir)
    except FileNotFoundError:
        print("Path does not exist")
    else:
        for file in result_list:
            entry = os.path.join(dir, file)
            yield entry


def gen_get_fline(file):
    with open(file, 'r') as f:
        for line in f:
            ret_str = line.strip(' \n\r\t')
            if ret_str == '':
                continue
            else:
                yield ret_str


def check_webpage(url):
    try:
        query = requests.get(url)
        if query.status_code == 200:
            return True
        else:
            return False
    except:
        return False


for file in gen_get_files("g:/py/exdata/links_to_check"):
    for line in gen_get_fline(file):
        exists_url = check_webpage(line)
        print("URL {0} Exists: {1}".format(line, exists_url))