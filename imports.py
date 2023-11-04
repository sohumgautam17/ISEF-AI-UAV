from random import choice 
from random import randint
from random import shuffle


coin = choice(["heads", "tails"])
print(coin)

number = randint(1, 10)
print(number)

names = ["Sohum", "Mihika", "Shivi"]
shuffle(names)
for i in names:
    print(i)
