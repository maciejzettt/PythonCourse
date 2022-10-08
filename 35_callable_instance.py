class NoDuplicates:

    def __init__(self):
        self.list = []

    def __call__(self, items):
        for t_item in items:
            if t_item not in self.list:
                self.list.append(t_item)
            else:
                pass

    def show(self):
        i = 1
        for t_item in self.list:
            print("{0}: {1}".format(i, t_item))
            i += 1


my_no_dup_list = NoDuplicates()

my_no_dup_list(['keyboard', 'mouse'])
my_no_dup_list.show()

my_no_dup_list(['keyboard', 'mouse', 'pendrive'])
my_no_dup_list.show()

my_no_dup_list(['charger','pendrive'])
my_no_dup_list.show()