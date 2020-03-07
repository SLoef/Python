import random

guess = 69
hidden = random.randrange(1, 20)

while guess != hidden:
    guess = int(input("Raadt het getal tussen 1 - 20"))

if guess == hidden:
    print("Je heb 'm Geraden!")

elif guess < hidden:
    print("Te laag")

else:
    print("Te hoog")
