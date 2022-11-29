import time


print("Welcome to the game, this game is about surviving and adventure")
print("Hit enter if you want to play")
e = input()
e != ""
time.sleep(0)
name = "kushal"
time.sleep(0)
print("Hey master" ,name,",\nYou're on a dirt trip and you've reached the end of the road,there's no way\nof going back cause, you know that saying 'darr ke aage, jeet hey',so you'll \nbe given two option please think properly and make it outta here.")
time.sleep(0)
print("Hit enter again to know more of the story")
e = input()
e!=""
print("So master",name,"you're on the end of the road, there's a river infront and bridge above it, which is slightly broken,\nwe never know when it'll fall off, so you've got two option either cross using bridge or swim by the river.")
print("Tools you have right now,\n1.Pistol, you'll be getting for tools coming up")
time.sleep(0)

while True:
    store = input("\tPlease decide properly, you're action also has a consequences.\t\nIf you want to Swim,\ntype 'swim'\t\nor type 'bridge' to use the bridge. =,").lower()
    if store == "bridge":
        print("You've made it inside the forest, let the journey begin")
        store = input("Now there's a road ahead of you do you want to go insie of it, hit enter").lower()
        if store == '':
            print("as we're walking by the bushy road, they bear spotted us and are following us")
            while True:
                store = input("do you want to fight at your own or climb the tree nearby or just kill him with the pistol?")
                if store == 'fight':
                    print("sorry your're dead")
                    break
                elif store == "climb":
                    print("your character doesnt know how to climb, youre dead")
                    break
                elif store == "pistol":
                    print("the bear has been dead you can continue your journey")
                    break
                else:
                    print("type properly")
        break
    if store == "swim":
        print("Haha, said by the hungry crocodile,\nYou're dead already, Game ended")
        break
    else:
        print("\tSorry, there's been a mistake, please type properly and try again")
        
