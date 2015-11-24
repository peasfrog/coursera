import urllib
import json

options = {
    "url": "http://python-data.dr-chuck.net/comments_42.json"
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
tree = json.loads(data)

for comment in tree['comments']:
    options['nodeCount'] += 1
    options['total'] += int(comment['count'])
# display output
print "Count: ", options["nodeCount"]
print "Sum: ", options["total"]
