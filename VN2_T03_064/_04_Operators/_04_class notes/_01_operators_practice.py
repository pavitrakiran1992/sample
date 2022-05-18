# #Arithmetic_operator:Used to perform mathematical operations
# x=10
# y=10
# z=x+y
# print(z)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x//y)
# print(x**y)
# print(x+y,x-y,x*y,x/y,x%y,x//y,x**y)
# #Assignment_Operators:used to assign values to variables
# x=20
# print(x)
# x+=10
# print(x)
# x=20
# x-=10
# print(x)
# x=200
# x*=10
# print(x)
# x=300
# x/=10
# print(x)
# x=150
# x//=10
# print(x)
# x=200
# x&=10
# print(x)
# x=50
# x^=5
# print(x)
# x=250
# x|=60
# print(x)
# x=600
# x>>=50
# print(x)
# x=300
# x<<=60
# print(x)
# #Comparision operators:used to compare two values/content in it
# x=50
# y=120
# print(x==y)
# print(x!=y)
# print(x>y)
# print(x<y)
# print(x<=y)
# print(x>=y)
# #Logical Operators:used to combine conditional statements
# #AND,OR,Not
# x=5
# y=3
# print(x>2 and y>2)  # True depending on 2nd case
# print(x>3 and y>4)  #False depending on 2nd case
# print(x<3 and y<4)  #False depending on 1st case
# print(x>7 and y>6)  #False depending on 1st case

# print(x > 2 or y > 2)  # True depending on 1st case
# print(x > 3 or y > 4)  # False depending on 1st case
# print(x < 3 or y < 4)  # False depending on 2nd case
# print(x > 7 or y > 6)  # False depending on 2nd case

# print(not(x>7 and y>6))
# print(not(x < 3 or y < 4))
# #Membership operators:used to find the membership in set,sequence
# #identity operators: used to the compare the memory location of two objects





print(4/2)
print(4 % 2)


print(10 != 12)


a = 10
ida = id(a)
b = 10
a = 20
c = 10
idc = id(c)
print(ida == idc)
print(a == b)
# counter += 1
# How memory management works in python

print(0 and 10) 
print(10 and False)


print(10 or False)
print(False and 10)

print(not (0 and 20))

print(10 in [1,2,4])


def some_function():
    return 'harsha'

a = some_function
print(a())

print(a is some_function)

# Models.query.filter(id = some_id).first()