# Functions
# print() - To print the given data in console
# type()  - To find the type of variable
# id()    - To find variable referring address
#int float complex bool
x = 10
print("Type of x : ", type(x))
print("Id of x   : ", id(x))

x = 10 + 20 - 45 * 43 / 2
print("Type of x : ", type(x))
print("Id of x   : ", id(x))

is_active = True
print("Type of is_active : ", type(is_active))
print("ID of is_active   : ", id(is_active))


# Type conversions
x = 10
print("----Type conversions--------")
'''
int()
float(x)
complex(a,b)
bool()
'''
x = 10
print("value : ",x, type(x))
# Convert to float
x = float(x)
print("value : ",x, type(x))


x = 1
print(x, type(x))
x = bool(x)
print(x, type(x))
print("-------------------")
x = 14
print(x, type(x))
x = bool(x)
print(x, type(x))
print("-------------------")
x = 0
print(x, type(x))
x = bool(x)
print(x, type(x))



eid = "10001"
print(eid, type(eid))

scan_code = 'abc32'
