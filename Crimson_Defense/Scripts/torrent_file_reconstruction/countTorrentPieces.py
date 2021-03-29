# used python3

import re

READ = open("pieces.txt", "r")

lines = READ.readlines()

count = 0

for line in lines:
    # using regex( findall() )
    # to extract words from string
    res = re.findall(r'\w+', line)

    for word in res:
        if(word == "Piece"):
            count += 1

print(count)
READ.close()
