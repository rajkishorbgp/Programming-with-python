for n in range(1, 101):
    if n % 2 != 0:
        print("Weird")
        break
    elif n in range(2, 6):
        if n % 2 == 0:
            print("Not Weird")
    elif n in range(6, 21):
        if n % 2 == 0:
            print("Weird")
    elif n > 20:
        if n % 2 == 0:
            print("Not Weird")
