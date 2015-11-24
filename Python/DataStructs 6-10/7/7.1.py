# Use words.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)

    for line in fh:
        line = line.rstrip()
        line = line.upper()
        print line

    fh.close()
except:
    print "%s not found." % (fname)
