import functools


class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, _name=None, _kind=None, _filling=None, _taste=None, _additives=None):
        if _additives is None:
            _additives = []
        self.name = _name
        if str(_kind).lower() in Cake.known_types:
            self.kind = _kind
        else:
            self.kind = 'other'
        self.filling = _filling
        self.taste = _taste
        self.additive = _additives
        Cake.bakery_offer.append(self)

    def show_info(self):
        print('=' * 30)
        print("Info for {0}".format(str(self.name).upper()))
        print('-' * 30)
        print("Taste:\t\t{0}".format(self.taste))
        if len(self.additive) == 0:
            print("No additions")
        else:
            print("Additions:")
            for ad in self.additive:
                print('\t\t\t{0}'.format(ad))
        if self.filling is not None:
            print("Filling:\t{0}".format(self.filling))
        print('=' * 30)

    def set_filling(self, new_filling):
        self.filling = new_filling

    @functools.singledispatchmethod
    def add_additive(self, new_additive):
        self.additive.append(new_additive)

    @add_additive.register(list)
    def _(self, new_additive):
        self.additive.extend(new_additive)


tort = Cake('Tort urodzinowy', 'cake', 'cream', 'strawberry', ['chocolate'])
babka = Cake('Babka świąteczna', 'brioche', None, 'butter', ['sugar glaze'])

tort.add_additive('almonds')
babka.add_additive(["raisins", "peanuts"])

for c in Cake.bakery_offer:
    c.show_info()
