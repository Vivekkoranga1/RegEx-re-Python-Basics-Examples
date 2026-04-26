##So in this from a text we will fetch all the valid email address.
##So first what is a valid email address.
## This is valid email format "local-part@domain.extension"

# 1. Local Part (before @)
# Allowed: letters(a-z,A-Z),numbers(1-10), . _ % + -
# Rules:
# cannot start or end with .
# no consecutive dots ..
#vivek123 (allowed)
#user.name (allowed)
#.vivek (not allowed) because start with .
#user..name (not allowed) because consecutive ..

# 2. @ Symbol
# Exactly one @ is required
#user@gmail.com (allowed)
#user@@gmail.com (not allowed) two "@@" not allowed

# 3. Domain (after @)
# domain.extension
# (a) Domain Name
# letters, numbers, hyphen -
# cannot start/end with -

# gmail (allowed)
# my-domain (allowed)
# -gmail (not allowed) cannot start with -

# (b) Extension (TLD)
# minimum 2 letters
# examples: .com, .org, .in

# .com (allowed)
# .edu (allowed)
# .c (not allowed) minimum 2 letters in extension 


import re

##down we have TEXT that i have copied from openai and we will valid email address from this 
TEXT = """While organizing the contact list, Vivek noticed that some emails like vivek@gmail.com
 and user.name123@yahoo.co.in
 looked perfectly fine, and even test_email+1@domain.org
 seemed valid. However, a few entries raised doubts, such as vivek@.com
 and @gmail.com, which clearly didn’t follow proper format. There were also confusing ones like user..name@gmail.com
 and vivek@gmail that seemed incomplete or incorrectly structured. Meanwhile, addresses like admin@company.com
 and hello.world@sub.mail.org
 appeared correct, but others like .username@yahoo.com
, user@domain.c
, and user@gmail..com looked suspicious. It became clear that identifying a valid email requires careful checking of both the local part and the domain structure."""




##pattern for local part
##[a-zA-Z0-9._%+-]+ so we are using "[]"" "character class" matches only one character from class
## inside "[]" "characterclass" . and + looses their ability 
##we are using "+" for atleast one and more should match inside character class
##See gamil want local part should be above 7 i guess and we can do that by using many thing  eq. {}but we are first doing basic 


##add @symbol
##[a-zA-Z0-9._%+-]+@
##add [a-zA-Z0-9-]+\. "\." for .
##[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.
##[a-zA-Z]{2,}
##[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}"
## with this pattern we will try to find all valid emails from Text
## Till now this is not corrected pattern because domain can start and end with  and can have consecutive "-"
## we will further improve it down 


all_valid_email = re.findall(pattern=pattern,string=TEXT)
for valid_email in all_valid_email:
    print(f"This is Valid email {valid_email}")
##OutPut
##There are many mistakes in our pattern and we want to improve it
##There are many limitation also because we are not checking one email we are checking from a TEXT
# This is Valid email vivek@gmail.com
# This is Valid email user.name123@yahoo.co
# This is Valid email test_email+1@domain.org
# This is Valid email user..name@gmail.com
# This is Valid email admin@company.com
# This is Valid email hello.world@sub.mail
# This is Valid email .username@yahoo.com




