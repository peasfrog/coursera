##Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day
# for each of the messages. You can pull the hour out
# from the 'From ' line by finding the time and then
# splitting the string a second time using a colon.

#Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.
#  0  |               1          | 2 | 3  |4|   5    | 6
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# 04 3

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = {}
#collect the from lines
for line in handle:
    if line.find('From ') == 0:
        line = line.strip()
        line = line.split()

        time = line[5].split(':')
        hour = time[0]

        # this makes incrementing easier
        hours[hour] = hours.get(hour, 0) + 1

handle.close()

#take the dict and sort it by value?
#turn into a list of tuples by key value
collector = []
for key, value in hours.items():
    collector.append((key, value))

collector.sort()

for hour in collector:
    print "%s %d" % (hour[0], hour[1])
