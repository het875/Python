#calculater using case 

calclulate = {
    "1" : "+",
    "2" : "-",
    "3" : "/",
    "4" : "*",
}

cal = input("Choose calclulater for the number \n   1. Sum\n   2. Minus\n   3. Multipul\n   4. Divison \nEnter number 1 to 4 :")

num1 = float (input("Enter a first NO: "))
num2 = float (input("Enter a secend No: "))

match cal :
    case "1":
        print(f"The sum of {num1} + {num2} = ",num1+num2)

    case "2":
        print(f"The minuse of {num1} - {num2} = ",num1-num2)

    case "3":
        print(f"The multi of {num1} * {num2} = ",num1*num2)

    case "4":
        print(f"The div of {num1} / {num2} = ",num1/num2)

    case defualt:
        print("invalid input")


"""
OUTPUT

Choose calclulater for the number
   1. Sum
   2. Minus
   3. Multipul
   4. Divison
Enter number 1 to 4 :20.2
Enter a first NO: 5
Enter a secend No: 3
invalid input



Choose calclulater for the number 
   1. Sum
   2. Minus
   3. Multipul
   4. Divison
Enter number 1 to 4 :3
Enter a first NO: 20.5
Enter a secend No: 2
The multi of 20.5 * 2.0 = 41.0
"""