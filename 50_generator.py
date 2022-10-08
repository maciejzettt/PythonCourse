
def GenerateSet(products, promotions, customers):
    for prod in products:
        for prom in promotions:
            for c in customers:
                yield "Product: [{0}] - Promotion: [{1}] - Customer: [{2}]".format(prod, prom, c)


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]

Set = GenerateSet(products, promotions, customers)

for s in Set:
    print(s)
