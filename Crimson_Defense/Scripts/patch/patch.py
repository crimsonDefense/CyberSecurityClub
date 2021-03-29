# Cole
#Goal of program is to run a bash command with every permutation of arguments
#This is useful for a file that has been split up as you can cat each permutation
#until you arrive at a file that passes some sort of validity check

import subprocess
from itertools import permutations
L = ["frag_1", "frag_2", "frag_3", "frag_5", "frag_6", "frag_7"]

for perm in permutations(L):
    temp = open("temp", "w")
    args = list(perm)
    args.insert(0, "frag_4") #Starting fragment to reduce possibilities
    args.insert(0, "cat") # Argument should now read 'cat file1 file2...'

    #Cat fragments together and write to temp
    subprocess.run(args, stdout=temp) 
    #Close file so we can work on it
    temp.close()
    #Make executable
    subprocess.run(['chmod', '+x', 'temp'])
    #Run it and write decoded result to variable
    result = subprocess.run(['./temp'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    #winner's pov
    if "FLAG" in result:
        print(result)
        quit()

    #clean up for next run
    subprocess.run(['rm', 'temp'])
