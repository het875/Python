#salab count

sal = float (input("Enter your Salary:"))


if (sal<=2500) :

    amt=sal

elif (sal<=5000) :

    amt=(sal*0.10)

elif (sal<=10000) :

    amt=(sal*0.20)

else :

    amt=(sal*0.30)


print(f"Your salary amount is : {amt:.2f}")

"""

OUTPUT


Enter your Salary:14000
Your salary amount is : 4200.00
"""