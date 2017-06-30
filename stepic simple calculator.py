x = float(input())
y = float(input())
z = str(input())
if z == "+":
	print (x+y)
elif z == "-":
	print (x-y)
elif z == "/" and not y == 0:
	print (x/y)
elif z == "*":
	print (x * y)
elif z == "mod" and not y == 0:
	print (x%y)
elif z == "pow":
	print (x**y)
elif z == "div" and not y == 0:
	print (x//y)
else:
	print ("Деление на 0!")