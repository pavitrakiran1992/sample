x = 10
y = 30
z= eval("5 ** 6")
print(z)
a =eval("x + y", {"x": x, "y": y})
print(a)
print(eval("x + y + z", {"x": x, "y": y, "z": 300}))
print(eval("min([1, 2, 3])", {}))