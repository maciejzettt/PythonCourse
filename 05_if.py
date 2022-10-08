import datetime

price = 1223
bonus = 23
bonus_granted = True

print(price - bonus) if bonus_granted else print(price)

rating = 5

print('very good') if rating == 5 else print('good') if rating == 4 else print("weak")


today = datetime.date.today().weekday()

if today == 0:
    print("Pomagam mamie")
elif today == 1 or 2:
    print("Pranie")
elif today == 3:
    print("Mam dyżur")
elif today == 4:
    print("Dwa zebrania")
elif today == 5:
    print("Lekcje")
else:
    print("NIEDZIELA JEST DLA NAS")

print("Pomagam mamie") if today == 0 else print("Pranie") if today == 1 or today == 2 \
    else print("Mam dyżur") if today == 3 \
    else print("Dwa zebrania") if today == 4 \
    else print("lekcje") if today == 5 else print("Niedziela jest dla nas!")

x=3
print("1 lub 2") if x == 1 or x == 2 else print("X")