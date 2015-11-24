import urllib
import re
from BeautifulSoup import *


def init():
    start = raw_input("Enter URL: ")
    ans = re.findall(r'(_[a-zA-Z]+)', start)
    # get the first name
    names = [ans[1][1:]]

    iterations = int(raw_input("Enter repeat: "))

    position = int(raw_input("Enter position: ")) - 1

    while iterations >= 0:
        if iterations > 0:
            print "Retrieving: " + start
            tags = makeSoup(start)
            #get the name
            tempName = tags[position].contents[0]
            # convert to raw string
            names.append(str(tempName))
            #get the next url
            start = tags[position].get('href')
        else:
            print "Last Url: " + start
        iterations = iterations -1

    print "Sequence of names: " + (", ").join(names)
    print "Last name in sequence: " + names[len(names)-1]


def makeSoup(url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    return soup('a')

init()



