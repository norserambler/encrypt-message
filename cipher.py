a = 'abcdefghijklmnopqrstuvwxyz0123456789'
encryp = ''#initialized an empty string
#msg = ''
msg = input("Enter the input: ")
key1 =input("Enter the key (integer): ")
key=int(key1)
for char in msg:
    pos = a.find(char)
    newpos = (pos + key)%36
    newchar = a[newpos]
    encryp += newchar 

print ("Encrypted msg is ",encryp)
