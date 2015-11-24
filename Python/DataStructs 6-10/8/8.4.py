fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    temp = line.split()
    # do another iteration here.
    for word in temp:
        try:
            lst.index(word)
        except ValueError:
            lst.append(word)

        lst.sort()
print lst