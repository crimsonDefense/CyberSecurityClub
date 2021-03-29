# used python3

import re
from ast import literal_eval

READ = open("pieces.txt", "r")
construct = open("reconstruct.txt", "w")

lines = READ.readlines()

torrent = {}
min = 100000
max = 0
count = 0
fcount = 0

for line in lines:
    # filtering out file, just want data
    pieces = re.search(r'\+.*\+', line)
    pieces = pieces.group().strip('+')
    pieces = pieces.split(',')
    # print(pieces)

    line = line.strip('+')
    data = re.search(r'\+.*\n', line)
    data = data.group().rstrip().strip('+')
    data = data.split(',')
    # print(data)

    i = 0
    for piece in pieces:
        dec = literal_eval(piece)

        if (dec > max):
            max = dec

        if(dec < min):
            min = dec

        torrent.update({dec:data[i]})
        fcount += 1
        i += 1

for i in range(min, max+1):
    x = torrent.get(i)
    construct.write(x)
    count += 1

print("Min was:", min)
print("Max was:", max)
print("fcount was", fcount)
print("count was", count)

READ.close()
