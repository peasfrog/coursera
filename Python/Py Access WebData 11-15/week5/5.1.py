import urllib
import xml.etree.ElementTree as Et

options = {
    "url": "http://python-data.dr-chuck.net/comments_42.xml"
    ,"nodeCount": 0
    ,"total": 0
}
# get input
userUrl = raw_input('Enter location: ')
if len(userUrl) > 1 :
   options['url'] = userUrl
# display output
print "Retrieving: ", options['url']

# get input
url = urllib.urlopen(options['url'])
data = url.read()
# display output
print "Retrieved ", len(data), "characters."

# get input
tree = Et.fromstring(data)
counts = tree.findall('.//count')
options['nodeCount'] = len(counts)
# display output
print "Count: ", options["nodeCount"]

# get input
for count in counts:
    options['total'] += int(count.text)
# display output
print "Sum: ", options["total"]
