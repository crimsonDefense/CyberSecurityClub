# takes in a string in all caps and prints every rotation for it 
  
text = input("Enter string in all caps for rot: ")
rot = 0
new = 0

while (rot < 26):
    for x in text:
        if ((ord(x) + rot) > 90):
            new = ((ord(x) + rot) % 90) + 64
        else:
            new = ord(x) + rot

        x = chr(new)
        print(x, end = "")

    print("\n")
    rot += 1
