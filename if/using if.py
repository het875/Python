# using if


number = input("Enter a number from 1 to 6: ")


if number == "1":
    print("Vanilla")

if number == "2":
    print("Chocolate")

if number == "3":
    print("Strawberry")

if number == "4":
    print("Coconut")

if number == "5":
    print("Mango")

if number == "6":
    print("Chikoo")
    
if number < "0" or number > "6" :
    print("Invalid number")

'''
Enter a number from 1 to 6: 7
Invalid number

Enter a number from 1 to 6: 6
Chikoo


'''