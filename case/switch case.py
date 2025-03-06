# switch case 
user_input = int(input("enter your lucky number between 1-5\n"))

match user_input:

        case 1:

            print( "you will have a new house")


        case 2:

            print( "you will receive good news ")


        case 3:

            print( "you will get a car")


        case 4:

            print( "you might face your fear this week")


        case 5:

            print( "you will get a pet")

        case default :
            print( "Invalid Number")


"""
OUTPUT

enter your lucky number between 1-5
5
you will get a pet

"""