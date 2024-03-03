x = int(input("Enter the number: "))

match x:
    case 0:
        print(x, "case is zero...")
    case 1:
        print(x, "case is one...")
    case 2:
        print(x, "case is two...")

    case _:
        print("else part")
