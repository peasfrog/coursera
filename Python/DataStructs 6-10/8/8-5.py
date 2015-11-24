fname = raw_input("Enter file name: ")

if len(fname) < 1 :
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    # print line.index('From')
    try:
        if line.index('From ') == 0:
            count += 1
            line.strip()
            words  = line.split()
            print words[1]
    except ValueError:
            continue
print "There were", count, "lines in the file with From as the first word"