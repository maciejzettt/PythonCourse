class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.maxitem = len(self.promotions)  * len(self.customers) * len(self.products) - 1

    def __getitem__(self, item):
        if item > self.maxitem:
            raise StopIteration
        elif item < 0:
            raise KeyError
        else:
            curr_product = item // (len(self.promotions)*len(self.customers))
            item2 = item % (len(self.promotions)*len(self.customers))
            curr_promo = item2 // len(self.customers)
            curr_cust = item2 % len(self.customers)
            return "{0} | {1} | {2}".format(self.products[curr_product], self.promotions[curr_promo], self.customers[curr_cust])


    # def __next__(self):
    #
    #     if self.current_customer >= len(self.customers):
    #         self.current_customer = 0
    #         self.current_promotion += 1
    #
    #     if self.current_promotion >= len(self.promotions):
    #         self.current_promotion = 0
    #         self.current_product += 1
    #
    #     if self.current_product >= len(self.products):
    #         self.current_product = 0
    #         raise StopIteration()
    #
    #     item_to_return = "{} - {} -{}".format(self.products[self.current_product],
    #                                           self.promotions[self.current_promotion],
    #                                           self.customers[self.current_customer])
    #
    #     self.current_customer += 1
    #
    #     return item_to_return
    #
    # def __iter__(self):
    #     return self


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]

combinations = Combinations(products, promotions, customers)

comb_itr = iter(combinations)
# for comb in range(30):
#     print(combinations[comb])
# print(next(comb_itr))
# print(next(comb_itr))
for c in comb_itr:
    print(c)

print(combinations[-3])