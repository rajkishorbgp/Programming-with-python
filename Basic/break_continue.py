friends=["Ram", "Rohan", "Raj", "Megha", "Manmeet", "Amarjeet"]

for i in friends:
    if i=="Megha":
        break
    print(i)

print("\nSecond list........")

for friend in friends:
    if friend=="Megha":
        continue
    print(friend)

#  Output
"""
Ram
Rohan
Raj

Second list........
Ram
Rohan
Raj
Manmeet
Amarjeet
"""