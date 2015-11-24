largest = None
smallest = None
listONums = []

while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
       #push into a list and sort the list
        listONums.append(num)

        listONums.sort()

        smallest = listONums[0]
        largest = listONums[len(listONums) - 1]


    except ValueError:
        print "Invalid input"
        continue


print "Maximum is ", largest
print "Minimum is ", smallest