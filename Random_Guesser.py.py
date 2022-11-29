import random

user = (input("Hi, its me Kush, this game is about guessing a number, if you want to try it out enter 'yes' or maybe 'no' if you dont want to.")).lower()

if user == "yes":
    print('welcome to the game, you"re given 10 chances.')
else:
    print("alright, closing")



a = random.randint(1,10)

def game1():
    for i in range(10):
        b = int(input("enter a number"))
        if b == a:
            print("you got it")
            quit()   
        else:
            print("no you didnt")
        if b<a:
            print("hint:you are lower")
        elif b>a:
            print("hint:you are higher")
game1()
print(a)