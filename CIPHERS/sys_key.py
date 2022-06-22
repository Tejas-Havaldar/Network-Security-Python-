# Name: Tejas Saiprasad Havaldar
# Batch: N6
# Roll No: 32230

print('Name: Tejas Saiprasad Havaldar')
print('Batch: N6')
print('Roll No: 32230')

def convert(s):
    str = ""
    return (str.join(s))

k1 = input('Enter the key at sender side')
k2 = input('Enter the key at receiver side')

if k1 == k2:
    print('Key matched')
    print("Let's get started")
    print()
    enc_text = input('Enter the input for encryption: ')
        
    d = []

    for i in range(len(enc_text)):
        xe = ord(enc_text[i]) + 3
        ye = chr(xe)
        d.append(ye)

    ae = convert(d)
    print("The encrypted text is: ",ae)

    dec_text = input('Enter the input for decryption: ')
        
    e = []

    for i in range(len(dec_text)):
        xd = ord(dec_text[i]) - 3
        yd = chr(xd)
        e.append(yd)

    ad = convert(e)
    print("The decrypted text is: ",ad)

else:
    print("key doesn't match" )