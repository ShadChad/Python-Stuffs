import time
score = 0

print("Hi, welcome to the game")
a = input("Do you wanna play, Enter Yes or No:").lower()
if(a == 'yes'):
    print("So, here the game goes")
    time.sleep(1)
else:
    print("im sorry")
    time.sleep(1)
    quit()
print("This game is about guessing the correct answer, Few questions will be given to you, and you may tell me the correct answer")


a = input(",Are you ready, Enter Yes or No:").lower()
if a == "no":
    print("We're closing the game")
    quit()
print("What is the capital city of Afghanstan?")
ans = input("Enter your answer here,:").lower()

if ans == "kabul":
    print("You've guessed it right")
    score = score + 1
    time.sleep(3)

else:
    print("Sorry, you got it wrong, its Kabul")
    time.sleep(3)

print("What is the capital city of India?")
ans = input("Enter your answer here,:").lower()

if ans == "delhi" or ans == "new delhi":
    print("You've guessed it right")
    time.sleep(3)
    score = score + 1
else:
    print("you got it wrong, its Delhi also New Delhi")
    time.sleep(3)

print("What is the capital city of Nepal")
ans = input("Enter your answer here,:").lower()
if ans == "kathmandu":
    print("You've guessed it right")
    score = score + 1
    time.sleep(3)
else:
    print("Sorry, you got it wrong, its Kathmandu")
    time.sleep(3)

print("What is the capital city of China?")
ans = input("Enter your answer here,:").lower()

if(ans == "beijing"):
    print("You've guessed it right")
    time.sleep(3)
    score = score + 1
else:
    print("You're Wrong, its Beijing")
    time.sleep(3)
print("What is the capital city of Japan?")
ans = input("Enter your answer here,:").lower()
score = score + 1
if(ans == "tokyo"):
    print("You've guessed it right")
    time.sleep(3)
    score = score + 1
else:
    print("Sorry, you got it wrong")
    time.sleep(3)

print("What is the capital city of Netherlands?")
ans = input("Enter your answer here,:").lower()

if(ans == "amsterdam"):
    print("You've guessed it right")
    time.sleep(3)
    score = score + 1

else:
    print("Sorry, you got it wrong")
    time.sleep(3)
print("What is the capital city of Protugal?")
ans = input("Enter your answer here,:").lower()

if(ans == "lisbon"):
    print("You've guessed it right")
    time.sleep(3)
    score = score + 1

else:
    print("Sorry, you got it wrong")
    time.sleep(3)

print("What is the capital city of Russia?")
ans = input("Enter your answer here,:").lower()

if(ans == "moscow"):
    print("You've guessed it right")
    time.sleep(3)
    score = score + 1

else:
    print("Sorry, you got it wrong")
    time.sleep(3)



print("You got " + str(score) + " questions correct")





