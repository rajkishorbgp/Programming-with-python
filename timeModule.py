import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp = int(time.strftime('%H'))
print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
if (timestamp < 12):
    print("Good Morning")
elif (timestamp < 21):
    print("Good evening")
else:
    print("Good night")
