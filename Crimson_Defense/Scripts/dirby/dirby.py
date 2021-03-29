# Cole
#Dirbuster-like script for sites that always return 301

import requests

###CUSTOM VALUES HERE###
host = "http://134.122.109.161:31071/"
error = "Error 404" #String to blacklist in result
outfile = "dirby.out"
#Can also change wordlist if desired
wordlist = open("/usr/share/wordlists/raft-small-directories.txt")

session = requests.Session()

output = open(outfile, "a")

for line in wordlist:
    r = session.get(host+line)
    if error not in r.text:
        print(line)
        output.write(line)


output.close()
wordlist.close()
