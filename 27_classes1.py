class Cake:

    def __init__(self, _name=None, _kind=None, _filling=None, _taste=None, _additives=None):
        if _additives is None:
            _additives = []
        self.name = _name
        self.kind = _kind
        self.filling = _filling
        self.taste = _taste
        self.additive = _additives

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

    def add_additive(self, new_additive):
        self.additive.append(new_additive)


tort = Cake('Tort urodzinowy', 'cake', 'cream', 'strawberry', ['chocolate', 'almonds'])
babka = Cake('Babka świąteczna', 'brioche', None, 'butter', ['sugar glaze'])

cakes = [tort, babka]
babka.add_additive("raisins")
tort.set_filling("orange cream")

for c in cakes:
    c.show_info()
