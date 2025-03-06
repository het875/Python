# Create a menu dictionary with prices as values
menu = {
    "1":250,
    "2":299,
    "3":30,
    "4":399,
    "5":50,
    "6":150,
    "7":20
}


print("1. Kaju masala\n2. Panir tika\n3. Roti\n4. Pizza\n5. Lava chocolate\n6. fries\nDrink")

dish = input("Enter a dish name: ")


match dish:
    case "1":
        print(f"The price of Kaju masala is {menu[dish]} rupees.")

    case "2":
        print(f"The price of Panir tika is {menu[dish]} rupees.")

    case "3":
        print(f"The price of Roti is {menu[dish]} rupees.")

    case "4":
        print(f"The price of Pizza is {menu[dish]} rupees.")

    case "5":
        print(f"The price of Lava chocolate is {menu[dish]} rupees.")

    case "6":
        print(f"The price of fries is {menu[dish]} rupees.")

    case "7":
        print(f"The price of Drink is {menu[dish]} rupees.")

    case _:
        print(f"{dish} is not in the menu.")

"""
OUTPUT

1. Kaju masala
2. Panir tika
3. Roti
4. Pizza
5. Lava chocolate
6. fries
Drink
Enter a dish name: 5
The price of Lava chocolate is 50 rupees.

"""