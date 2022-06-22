# Name: Tejas Saiprasad Havaldar
# Batch: N6
# Roll No: 32230

print('Name: Tejas Saiprasad Havaldar')
print('Batch: N6')
print('Roll No: 32230')

import hashlib

str = "PICTPUNE"

# encoding PICT PUNEusing encode()
# then sending to SHA256()
result = hashlib.sha256(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())

print ("\r")

str = "PICTPUNE"

# encoding PICTPUNE using encode()
# then sending to SHA384()
result = hashlib.sha384(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA384 is : ")
print(result.hexdigest())

print ("\r")

str = "PICTPUNE"

# encoding PICTPUNE using encode()
# then sending to SHA224()
result = hashlib.sha224(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA224 is : ")
print(result.hexdigest())

print ("\r")

str = "PICTPUNE"

# encoding PICTPUNE using encode()
# then sending to SHA512()
result = hashlib.sha512(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA512 is : ")
print(result.hexdigest())

print ("\r")

str = "PICTPUNE"

# encoding PICTPUNE using encode()
# then sending to SHA1()
result = hashlib.sha1(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())