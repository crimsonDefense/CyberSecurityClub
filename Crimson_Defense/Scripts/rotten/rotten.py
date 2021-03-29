# Cole
#Custom caesar/rotation cipher solver with custom alphabet

#Built-in sets to build from
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

###DEFINE VALUES HERE###
alphabet = lower+nums #define sets you wish to use and what order
ciphertext = "28x3j18zb91pg41jne80n2zelcun" 
known_term = "flag" #term to find in plaintext


def inc(char, alphabet, num): #char incrementer
    index = alphabet.index(char)
    return alphabet[(index+num)%len(alphabet)]

cipher = ciphertext #using separate variable so we can check for no solution
while known_term not in cipher:
    cipher = list(cipher) #setting to list for mutability
    for index in range(0,len(cipher)):
        cipher[index] = inc(cipher[index], alphabet, 1)
    cipher = "".join(cipher) #joining back to list for checking/printing
    if cipher == ciphertext: #rotated back to original
        print("No match")
        exit()
    print(cipher) #progress and solution
