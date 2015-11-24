import urllib
from BeautifulSoup import *

html = urllib.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_186190.html').read()
# html = urllib.urlopen('http://dr-chuck.com').read()
soup = BeautifulSoup(html)

tags = soup('span')
count = 0
# print tags
for tag in tags:
    # Look at the parts of a tag
    count = count + int(tag.contents[0])

print 'Count: %d' % (count)
