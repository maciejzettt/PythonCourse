import itertools as it
import os


def scantree(path):
    for e in os.scandir(path):
        if e.is_dir():
            yield e
            yield from scantree(e)
        else:
            yield e


listing = scantree("G:/py/")
listing_dir = []
for l in listing:
    listing_dir.append({'type': "DIR" if l.is_dir() else "FILE", 'path': l.path})

listing_dir = sorted(listing_dir, key=lambda x: x['type'])

listing_summary = it.groupby(listing_dir, key=lambda x: x['type'])
for key, e in listing_summary:
    print(key, list(e))
