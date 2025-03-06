#bill unit

unit = float (input("enter your bill unit: "))

if (unit<100) :
    bill=(unit*0.60)

elif(unit<=300) :
    bill=(60+((unit-100)*0.80))

else :
    bill=(220+((unit-300)*0.90))

if (bill<=50):
    bill=50
    print("%0.2f\n",bill)

elif(bill>300):
    bill+=bill*0.15
    print("%0.2f\n",bill)

else:
    printf("%0.2f\n",bill)
