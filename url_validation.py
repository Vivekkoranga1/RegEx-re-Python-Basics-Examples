import re

##good pattern not more strict
pattern = r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(\/\S*)?$'

url = input("Enter a Url: ")

if re.match(pattern, url):
    print("Valid URL")
else:
    print("Invalid URL")


###pattern explain
# ^ → start of string
# (https?:\/\/)? → optional http:// or https://
# (www\.)? → optional www.
# [a-zA-Z0-9-]+ → domain name
# \. → dot
# [a-zA-Z]{2,} → domain extension (.com, .org, etc.)
# (\/\S*)? → optional path
# $ → end of string