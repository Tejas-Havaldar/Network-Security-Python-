import sys

def convert(s):
    str = ""
    return (str.join(s)) 

while True:
    choice_num = int(input("If you want to Encrypt the text then enter 1\nIf you want to Decrypt the text then enter 2: \n"))

    if choice_num == 1:
        enc_text = input('Enter the input for encryption: ')
        
        d = []

        for i in range(len(enc_text)):
            xe = ord(enc_text[i]) + 7
            ye = chr(xe)
            d.append(ye)

        ae = convert(d)
        print("The encrypted text is: ",ae)

        conti_num = int(input("If you want to continue enter 1 \nIf you want to end 2: \n"))
        if conti_num == 1:
            continue
        if conti_num == 2:
            exit()


    if choice_num == 2:
        dec_text = input('Enter the input for decryption: ')
        
        e = []

        for i in range(len(dec_text)):
            xd = ord(dec_text[i]) -7
            yd = chr(xd)
            e.append(yd)

        ad = convert(e)
        print("The decrypted text is: ",ad)

        conti_num = int(input("If you want to continue enter 1 \nIf you want to end 2: \n"))
        if conti_num == 1:
            continue
        if conti_num == 2:
            exit()
