import random


def random_sum(numberOfValues, TargetSum, numberOfMixes):
    listOfValues = []
    for i in range(numberOfMixes):
        trial = 0
        while True:
            trial += 1
            listOfValues.clear()
            for i in range(numberOfValues):
                listOfValues.append(random.randint(1, TargetSum))
            if sum(listOfValues) == TargetSum:
                break
            else:
                continue
        yield (trial, listOfValues)


for s in random_sum(3, 100, 50):
    print(s)
