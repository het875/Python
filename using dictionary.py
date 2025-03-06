#usinr dictionary
flavors = {
    '1' : 'Vanilla',
    '2' : 'Chocolate',
    '3' : 'Strawberry',
    '4' : 'Coconut',
    '5' : 'Mango',
    '6' : 'Chikoo'
}


key = input("Enter a key from 1 to 6: ")

if key in flavors:
    print(flavors[key])
    
else:
    print("Invalid key")

"""
Enter a key from 1 to 6: 5
Mango

"""