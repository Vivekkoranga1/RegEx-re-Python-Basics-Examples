import re


##for basics check previous commit and basics.py
text = input("Enter email address to Check : ")

##Standard pattern but not universal
pattern = r"^(?!\.)(?!.*\.\.)[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+(?<!\.)@[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*(?:\.[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)*\.[A-Za-z]{2,}$"


valid =re.search(pattern=pattern,string=text)

if valid:
    print(f"Sir , your email address {text} is valid.")
else:
     print(f"Sir , something wrong is with you email address {text}")
    
    




