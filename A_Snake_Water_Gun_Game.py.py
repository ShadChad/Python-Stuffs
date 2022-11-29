import random

def swg(comp,mine):
    if comp == 's' and mine == 'g':
        return True
    elif comp == 'w' and mine =='s':
        return True
    elif comp == 'g' and mine =="w":
        return True
    elif comp == mine:
        return None
    else:
        return False

choice = ("s","w","g")
comp = random.randint(0,2)
comp = choice[comp]
print(comp)
mine = input("enter a key")

win = swg(comp,mine)
if win is None:
    print('match draw')
elif win:
    print("you won")
else:
    print("lose")
