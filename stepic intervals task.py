x = int(input())
if -15 < x <= 12:
	print (True)
elif 14 < x < 17:
	print (True)
elif x >= 19:
	print (True)
else:
	print (False)

# shorter way to solve the same problem:

x = int(input())
if -15 < x <= 12 or 14 < x < 17 or x >= 19:
	print (True)
else:
	print (False)