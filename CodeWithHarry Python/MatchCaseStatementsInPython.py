value = int(input("enter a value"))
match value:
    case 21:
        print("you pressed 21")
    case 5:
        print("u pressed 5")
    case _:
        print("This is default case")