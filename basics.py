##String-Processing/Text-Processing
##1.Regular Expression     2.Wildcards in Python

##In this Repo and Project we are only going to focus on Regular Expression Because they are Advance then wildcards and more important 
##1Regular Expression
##For Regular Expression in python  we use "re" Module 
##Main Uses of Regular Expression
# Validation (email, phone) eg.Checking like email must contain '@' and 'gmail.com' 
# Data extraction eg. find the matching pattern from paragraph
# Search & replace eg. printing passwod but *** format


## Understanding how to use re module 
import re 

##text from where we need to find things
text = "Hello I am vivek . I am from India and i am part of Stanford Code in place 2026"



#finds first occurrence using "Search"
##keep in mind search finds the occurence
find_first_I = re.search(pattern="I",string=text)
print(find_first_I)
##OutPut:<re.Match object; span=(6, 7), match='I'>
##match='I' → what was found
##span=(6,7) → position in string
##to print the word we find use .group() search finds the word and group gives use word
word_we_find = find_first_I.group()
print(word_we_find)
##OutPut:I
##Finding start postion in text
start_index_of_word = find_first_I.start() 
print(start_index_of_word)
##OutPut:6
##Finding end postion in text
end_index_of_word =find_first_I.end()
print(end_index_of_word)
##OutPut:7
##What if we try to find not present word
finding_not_present_word = re.search("Harvard",string=text)
print(finding_not_present_word)
##Output:None
##What if we try to find small Vivek but vivek v with smallcase present in text
##it will give None 
##but if we use flags parameter and give re.IGNORECASE argument now it will ignore case wether big or small 
using_ignore_case = re.search(pattern="Vivek",string=text,flags=re.IGNORECASE)
print(using_ignore_case)
##OUTPUT:<re.Match object; span=(11, 16), match='vivek'>




 
##Using "findall" to find all occurences:
find_all_I = re.findall(pattern="I",string=text)
print(find_all_I)
#OUTPUT ['I', 'I']




##Checking "text" is starting from "Hello" or not using "Match" (It checks ONLY at the start of the string) unlike in powershell it matches the pattern 
check_text_start_with_Hello = re.match("Hello",string=text)
print(check_text_start_with_Hello)
##OutPut:<re.Match object; span=(0, 5), match='Hello'>
check_text_start_with_Vivek = re.match("Vivek",string=text)
print(check_text_start_with_Vivek)
##OutPut:None Because text does not start with Vivek





##Replacing word with another word in text we have vivek and i am replacing it with VivekSinghKoranga using "sub"
new_text = re.sub("vivek", "VivekSinghKoranga", text)
print(new_text)
##Output:Hello I am VivekSinghKoranga . I am from India and i am part of Stanford Code in place 2026


##see now we have done the basic things and understand basic concepts of regular expressions and basic methods and functions of re module
##Instead of matching exact text, now we can try to match types of text using "Meta Character"
##Meta characters = special symbols that give meaning to patterns

# # Common Regular Expression Metacharacters
# # These characters are used to define search patterns: 
# # . (Dot): Matches any single character except a newline.
# # ^ (Caret): Matches the start of a string or line.
# # $ (Dollar Sign): Matches the end of a string or line.
# # * (Asterisk): Matches zero or more occurrences of the preceding character.
# # + (Plus): Matches one or more occurrences.
# # ? (Question Mark): Matches zero or one occurrence.
# # \ (Backslash): Escapes a character, treating it as a literal rather than a special character.
# # [] (Square Brackets): Defines a character class/set (e.g., [a-z]).
# # | (Pipe): Acts as an OR operator (e.g., A|B).
# # () (Parentheses): Groups characters for capture.
##{} (Curly Braces): Specifies a quantifier (number of occurrences). 


##now we will use each meta character to find words from text and we are using same text 
##text = "Hello I am vivek . I am from India and i am part of Stanford Code in place 2026"

using_dot = re.findall(pattern="viv.k",string=text)
print(using_dot)
##OutPut:['vivek'] see i am not writing e in viv.k because "."(Dot): Matches any single character except a newline."
##See if now i want to find the real dot "."
##"." means any character, NOT a real dot
##For real dot 
# for_this	|   use_this 
# .	        |    \.
# +	        |    \+
# *	        |    \*
# ?	        |    \?

##way to find real dot "." using backslash "\"
## "." "+" "*" "?" are special character so when we use \ like "\." we escape the special character and also use for making special sequences
find_dot = re.findall(pattern="\.",string=text)
print(find_dot)
#Ouptput:['.']


##THE IDEA OF RAW STRING 
##we are working with special charcters and meta data but we can face some problem like 
##"\n" this give us new line and "\b" this is used for back slash 
##but when we try to use them in RegularExpression python process them before they reach to "RegularExpressions"
##so we use raw string FORMAT = r"" or R""
##We use raw strign because we dont want future problem 
##e.g 
##with raw string 
print(r"Hello\nWorld")
##Output:Hello\nWorld
##without raw string 
print("Hello\nWorld")
##Output:Hello
##World


##it is part of meta character
# # \ (Backslash): Escapes a character, treating it as a literal rather than a special character.
##for escaping "\n" new line we can also use ("\\n" "\\" become "\") 
print("Hello\\nWorld")
##OutPut:Hello\nWorld
print("Hello\\World")
##Output:Hello\World
print("Hello\nWorld")
##OutPut:Hello
##World



##Use  of ^ (Caret)
##Matches the start of a string or line. work like re.match we have already read above
star_with_Hello_using_caret = re.findall(r"^Hello",string=text)
print(star_with_Hello_using_caret)
##Output:['Hello']



# # $ (Dollar Sign): Matches the end of a string or line.
##eg. checking 2026 coming at the end of text or not 
check_2026_at_end_using_dollar = re.findall(r"2026$",text)
print(check_2026_at_end_using_dollar)
##output:['2026']


# # * (Asterisk): Matches zero or more occurrences of the preceding character.
new_text_for_asterisk = "bbbbbbb"
##many occurence
print(re.findall(r"b*",new_text_for_asterisk))
##Output:['bbbbbbb', ''] it also give '' because it zero or more matches no match also give ''
##zero match 
print(re.findall("a*","bbbbbbbbbbbbbbbbb"))
##output:['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''] ## every time 0 match so it give ""...
##WE WILL DO ADVANCE THINGS IN PROJECT HERE WE ARE LEARNING BASICS




# # + (Plus): Matches one or more occurrences.
##if zero_occurence
print(re.findall(r"b+",string="aaaaaaaa"))
# Output:[]
##if one occurence
print(re.findall(r"b+",string="aaaaaaab"))
# Output:['b']
##if more occuernce
print(re.findall(r"b+",string="bbbbbbb"))
#Output:['bbbbbbb']



# # ? (Question Mark): Matches zero or one occurrence.
##if zero_occurence
print(re.findall(r"b?",string="aa"))
##Output:['', '', ''] it try to check b in aa then it will move forward and check but there is nothing so it also match to 0 times that's why '' coming three times
##if one occurence
print(re.findall(r"b?",string="b"))
##Output:['b', '']
##if one occurence
print(re.findall(r"b?",string="bbbbb"))
##Output:['b', 'b', 'b', 'b', 'b', '']




# # [] (Square Brackets): Defines a character class/set (e.g., [a-z]).
print(re.findall(r"[a-z]",text,flags=re.IGNORECASE))
##OutPut:['H', 'e', 'l', 'l', 'o', 'I', 'a', 'm', 'v', 'i', 'v', 'e', 'k', 'I', 'a', 'm', 'f', 'r', 'o', 'm', 'I', 'n', 'd', 'i', 'a', 'a', 'n', 'd', 'i', 'a', 'm', 'p', 'a', 'r', 't', 'o', 'f', 'S', 't', 'a', 'n', 'f', 'o', 'r', 'd', 'C', 'o', 'd', 'e', 'i', 'n', 'p', 'l', 'a', 'c', 'e']
##we are getting everything except 2026
##better approach
print(re.findall(r"[a-z]+",text,flags=re.IGNORECASE)) ##matching one or more 
##Output ['Hello', 'I', 'am', 'vivek', 'I', 'am', 'from', 'India', 'and', 'i', 'am', 'part', 'of', 'Stanford', 'Code', 'in', 'place']





##| (Pipe): Acts as an OR operator (e.g., A|B).
print(re.findall(r"vivek|code",text,flags=re.IGNORECASE))
##Output['vivek', 'Code']


# # () (Parentheses): Groups characters for capture.
##with parenthesis 
print(re.findall(r"(ab)+","ab abb abbb abab ababab")) ## here one or more number of ab 
##output:['ab', 'ab', 'ab', 'ab', 'ab']
##without parenthesis 
print(re.findall(r"ab+","ab abb abbb abab ababab")) ## wher ab or abb or abbb like that 
##output:['ab', 'abb', 'abbb', 'ab', 'ab', 'ab', 'ab', 'ab']




##{} (Curly Braces): Specifies a quantifier (number of occurrences). 
##exact match
print(re.findall(r"a{2}", "a aa aaa"))
##Output:['aa', 'aa']



##See i want to tell you that we can find words or text using normal pattern but we use "meta characters" for validation"
##like from a paragrah finding all the valid emails and valid mobile numbers
## like college use for while accessing their portal it should exactly match @particularcollege.com
##we will do many examples related to validation like email and phone number validation in this repository. 