# day wise

week = {
    "1" : "Monday",
    "2" : "Tuesday",
    "3" : "wednesday",
    "4" : "thursday",
    "5" : "friday",
    "6" : "saturday",
    "7" : "sunday"
}


day = input("Enter day 1 to 7 : ")

match day :
    case "1" :
        print(f"This is a {week[day]}")
    case "2" :
        print(f"This is a {week[day]}")
    case "3" :
        print(f"This is a {week[day]}")
    case "4" :
        print(f"This is a {week[day]}")
    case "5" :
        print(f"This is a {week[day]}")
    case "6" :
        print(f"This is a {week[day]}")
    case "7" :
        print(f"This is a {week[day]}")
    case defualt :
        print(f"This is day {day} is invalid day.")

"""
OUTPUT

Enter day 1 to 7 : 12
This is day 12 is invalid day.

Enter day 1 to 7 : 5
This is a friday


"""