# used python3

import re

READ = open("rawOutput.txt", "r")
construct = open("pieces.txt", "w")

lines = READ.readlines()

frames = 0

for line in lines:
    frames += 1
    res = re.search(r'\+0x.*', line)
    data = res.group()
    construct.write(data)
    construct.write('\n')

print("Done. number of frames were:", frames)
READ.close()
