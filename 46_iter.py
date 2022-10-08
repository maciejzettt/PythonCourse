import time

products = ["Product {}".format(i) for i in range(1, 500)]
print(products)

promotions = ["Promotion {}".format(i) for i in range(1, 50)]
print(promotions)

customers = ['Customer {}'.format(i) for i in range(1, 500)]
print(customers)


class Combinations:

    def __init__(self, products:list, promotions:list, customers:list):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.cur_prod = 0
        self.cur_prom = 0
        self.cur_cust = 0
        self.max_prod = len(self.products)
        self.max_prom = len(self.promotions)
        self.max_cust = len(self.customers)

    def __next__(self):
        if self.cur_cust >= self.max_cust:
            self.cur_cust = 0
            self.cur_prom += 1
        if self.cur_prom >= self.max_prom:
            self.cur_prom = 0
            self.cur_prod += 1
        if self.cur_prod >= self.max_prod:
            self.cur_prod = 0
            raise StopIteration
        ret_item = self.products[self.cur_prod] + self.promotions[self.cur_prom] + self.customers[self.cur_cust]
        self.cur_cust += 1
        return ret_item

    def __iter__(self):
        return self


combinations = Combinations(products, promotions, customers)
for c in combinations:
    pass
