import csv

with open('g:/py/exdata/dok.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print('|'.join(row))
    while True:
        try:
            print(next(csvreader))
        except StopIteration:
            print("++koniec pliku++")
            break
