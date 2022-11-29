


while True:
    while True:
            
            num1 = (input("ENTER A NUMBER"))
            num2 = (input("ENTER A SECOND NUMBER"))
            if num1.isdigit() and num2.isdigit():
                sum = int(num1)
                sum1 = int(num2)
                
                print("what operation you want to perform,the keywords are a s d m for additin subtraction division and multiplication resp.")
                break
            else:
                print("Error occured, Please enter the number again")
    while True:
        calculate = input("enter a  keywords")
        if calculate == "a":
            print(f"The sum is, {sum + sum1} ")
            break 
        else:
            print("Error occured, please enter again")
        if calculate == "s":
            print(f"The result is, {sum-sum1}")
            break
        elif calculate == "d":
            print(f"The result is,{sum/sum1}")
            break
        elif calculate == "m":
            print(f"the product is,{sum*sum1}")
            break
        
        
    print("thank you for using the calculator, its only a prototype,hit enter to use the calcutor again")

    e = input()
    if e !='':
        break
