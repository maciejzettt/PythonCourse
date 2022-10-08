import functools


class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, _name=None, _kind=None, _filling=None, _taste=None, _additives=None, _gluten_free=False, _text=''):
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
        self.__gluten_free = _gluten_free
        Cake.bakery_offer.append(self)
        self.__text = ''
        self.__set_text(_text)

    def show_info(self):
        print('=' * 30)
        print("Info for {0}".format(str(self.name).upper()))
        print('-' * 30)
        print("GLUTEN FREE" if self.__gluten_free else "WITH GLUTEN")
        print("Taste:\t\t{0}".format(self.taste))
        if len(self.additive) == 0:
            print("No additions")
        else:
            print("Additions:")
            for ad in self.additive:
                print('\t\t\t{0}'.format(ad))
        if self.filling is not None:
            print("Filling:\t{0}".format(self.filling))
        print("Text:\t\t{0}".format(str(self.Text)))
        print('=' * 30)

    def set_filling(self, new_filling):
        self.filling = new_filling

    @functools.singledispatchmethod
    def add_additive(self, new_additive):
        self.additive.append(new_additive)

    @add_additive.register(list)
    def _(self, new_additive):
        self.additive.extend(new_additive)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind.lower() == 'cake' or new_text == '':
            self.__text = new_text
        else:
            print("{0} [{1}]: Cannot set text to anything other than cakes.".format(self.name, self.kind))

    Text = property(__get_text, __set_text, None, "Sets a new text to appear on a cake")


tort = Cake('Tort urodzinowy', 'cake', 'cream', 'strawberry', ['chocolate'], False, "Niespodzianka")
babka = Cake('Babka świąteczna', 'brioche', None, 'butter', ['sugar glaze'], False, "A to babka")
beza = Cake('Beza', 'other', None, 'Sugar', None, True, "")

for c in Cake.bakery_offer:
    c.show_info()

beza.__gluten_free = False
beza.show_info()
