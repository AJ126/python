# Write a Python Program to check whether the given mail id is valid gmail id or not

import re 
s=input("Enter Mail id:")
m=re.fullmatch("\\w[a-zA-Z0-9_.]*@gmail[.]com",s) 
if m!=None:
    print('Valid mail id', s)
else:
    print('Invalid mail id')