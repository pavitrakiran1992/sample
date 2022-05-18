a,b,c = 30,4,5

print(a,b,c)
print(type(a))
total =0
total = a+b
print(total)
a = 5.6
print(type(a))
x = 'pavitra'
print(type(x))
z = 2+4j
print(type(z))
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
cities = ["tirupathi", "bangalore", "chennai"]
x, y, z = cities
print(x)
print(y)
print(z)
_0ty = 5
print(_0ty)
x = "awesome"
#global key word
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)



