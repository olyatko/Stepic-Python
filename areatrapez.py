def problem1_7(base, otherbase, height):
    base = raw_input("Enter the length of one of the bases: ")
    otherbase = raw_input("Enter the length of the other base: ")
    height = raw_input("Enter the height: ")
    areatr = (1/2) * (base + otherbase) * height
    print ("The area of a trapezoid with bases " + str(base) + "and " + str(otherbase) + "and height " + str(height) + "is " + str(areatr)
