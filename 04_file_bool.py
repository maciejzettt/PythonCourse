import os


def FileWordCount(p):
    fl = open(p, mode='r')
    fl_txt = fl.read()
    fl_words = fl_txt.split()
    return len(fl_words)


path = "G:/py/44.txt"
if os.path.isfile(path):
    print(FileWordCount(path))

