# Array
list=[4,3,2,5,6,"raj"]

print(list) #print all

print(list[0]) # 0th indx print

print(list[-1]) #last element

print(list[0:4]) # range to print

list.append(10) # add to last
print(list)

list.insert(0,11) # add to indx element
print(list)

print(len(list))


print("print array")
i=0
while i < len(list):
    print(list[i])
    i=i+1
print("clean all element")
list.clear()  # clear the array
print(list)
print(len(list))
