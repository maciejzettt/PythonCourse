import functools


class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    def __str__(self):
        return "{0} is a {1} with {2}.".format(self.name, self.kind, self.additives)

    @functools.singledispatchmethod
    def __add__(self, other):
        raise Exception("Only str literals can be used")

    @__add__.register(str)
    def _(self, other):
        self.additives.append(other)

    @__add__.register(list)
    def _(self, other):
        for i in other:
            self + i


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
print(cake01)
cake01 + ["12", "dodatek", ["lista1", "lista2"]]
print(cake01)