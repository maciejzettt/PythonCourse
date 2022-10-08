class Cake:
    """A class describing a cake."""
    bakery_offer = []

    def __init__(self, name: str, kind: str, taste: str, additives: list, filling: str):
        """Cake init: \n
        name:str - name of a cake; \n
        kind:str - kind of a cake; \n
        taste:str - tase of a cake; \n
        additives:list - additives; \n
        filling:str - filling of a cake"""
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

    @property
    def full_name(self):
        """Returns a formatted full name of a cake"""
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

Cake()