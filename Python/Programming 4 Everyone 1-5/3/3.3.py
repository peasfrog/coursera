numIn = raw_input("Enter a Number between 0.0 and 1.0: ")

try:
    numIn = float(numIn)
except:
    print "Input was not a number between 0.0 and 1.0"
    exit()

if not (0.0 <= numIn <= 1.0):
    print "Number out of Range. Please try again later. Good bye."
elif numIn >= 0.9:
    print "A"
elif numIn >= 0.8:
    print "B"
elif numIn >= 0.7:
    print "C"
elif numIn >= 0.6:
    print "D"
else:
    print "F"