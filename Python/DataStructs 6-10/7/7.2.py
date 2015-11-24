# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
    numberOfMatches = 0
    totalConfidence = 0

    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        #increase sum of confidence
        totalConfidence += float(line[19:])
        #increase total number of matches
        numberOfMatches += 1

    # Average spam confidence: 0.750718518519
    #format the float to 12 places....185185185R
    print "Average spam confidence: %.12f" % (totalConfidence/numberOfMatches)

except:
    print '%s was not found.' % (fname)