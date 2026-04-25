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

