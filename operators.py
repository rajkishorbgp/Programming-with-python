
a = 20
b = 10

# 1. Arithmetic operators
print("Add: ", a+b)
print("Subtract: ", a-b)
print("Multiply: ", a*b)
print("Divide: ", a/b)

# 2. Assighment operators
a = b
print("a=b: ", a)
a += b
print("a+=b", a)
a -= b
print("a-=b", a)
a *= b
print("a*=b", a)
a /= b
print("a/=b", a)
a %= b
print("a%=b", a)

# 3. Comporision Operators
print("\na= ", a, "\nb= ", b)
print("\na==b -> ", a == b)
print("a<b -> ", a < b)
print("a>b -> ", a > b)
print("a!=b -> ", a != b)
print("a<=b -> ", a <= b)
print("a>=b -> ", a >= b)

# 4. Logical operators
a = True
b = False
print("\na = ", a, "\nb = ", b)
print("\na and b -> ", a and b)
print("a or b -> ", a or b)
print("not a -> ", not a)


'''
Output:
Add:  30
Subtract:  10
Multiply:  200
Divide:  2.0
a=b:  10
a+=b 20
a-=b 10
a*=b 100
a/=b 10.0
a%=b 0.0

a=  0.0
b=  10

a==b ->  False
a<b ->  True
a>b ->  False
a!=b ->  True
a<=b ->  True
a>=b ->  False

a =  True
b =  False

a and b ->  False
a or b ->  True
not a ->  False

'''
