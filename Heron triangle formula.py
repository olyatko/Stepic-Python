a = int (input())
b = int (input())
c = int (input())
p = (a + b + c) * 0.5
S = (p * (p - a) * (p - b) * (p - c))**0.5
print (S)

# math.sqrt(x) is the same as x**0.5

a, b, c = int(input()), int(input()), int(input())
p = (a + b + c) * 0.5
print ((p * (p - a) * (p - b) * (p - c))**0.5)
