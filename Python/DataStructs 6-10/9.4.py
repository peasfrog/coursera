name = raw_input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

senders = dict()

for line in handle:
    if line.find('From ') == 0 :
        line = line.strip()
        line = line.split()
        sender = line[1]

        if sender in senders:
            senders[sender] += 1
        else:
            senders[sender] = 1
    else:
        continue
handle.close()

maxVal = 0
chatterbox = ""
for key in senders:
    sentMsgs = senders[key]
    if sentMsgs > maxVal:
        maxVal = sentMsgs
        chatterbox = key

print chatterbox, senders[chatterbox]
