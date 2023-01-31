# Sping_2023_CRN_59000-08_NLP_Homework1_By_Prasad_Mahabare
# Under guidance of Professor Jonathan Rusert

import re   # Regular Expression Library
import io   # For File read and write operations
import codecs   # Converting the output to UTF-8
import string   # For string operations such as punctuation

# Initializing the file
filepath = 'The_War_Of_The_Worlds.txt'
# Reading the ilepathinput file which is "Plain Text UTF-8"
with io.open(filepath,'r', encoding='utf8') as f: file = f.read()

readed_file = file

def process_regex(input):

    # Iterating through the input string
    while(input):
        # Mr to Mister
        input= re.sub(r"Mr.", "Mister", input)

        # Ms to Miss
        input = re.sub(r"Ms.","Miss",input)

        # Mrs to Missus / Mistress
        input = re.sub(r"Mrs","Missus",input)

        # Dr to Doctor
        input = re.sub(r"Dr.","Doctor",input)

        # Britsh English words to American Enlish words
        input = re.sub("(^[^v]\w\w+our\b)((labour))","$1or\b",input) # our -> or

        # Single person am, me, my
        input = re.sub(r"(\bam\b)|(Me\b|\bme\b)|(My\b|\bmy\b)","",input)

        # Remove initials H. G. Wells
        input = re.sub(r"(\w\.\s\w\.)","",input)

        # Single letter I, a
        input = re.sub(r"(^\w\s)","",input)

        # Removing independent letters
        input = re.sub(r"^\w\b","",input)

        # Two letter supporting words so, of, at, or, at, to, in, it, is, as, an
        input = re.sub(r"(so\b)|(\bof\b)|(\bOR\b|\bOr\b|\bor\b)|(At\b|\bat\b)|(To\b|to\b)|(IN\b|In\b|\bin\b)|(It\b|\bit\b)|(Is\b|\bis\b)|(As\b|\bas\b)|(An\b|\ban\b)","",input)

        # Three and four letter supporting words and, with, for, its
        input = re.sub(r"(And\b|and\b)|(With\b|with\b)|(For\b|for\b)|(Its\b|\bits\b)","",input)

        # Other supporting words U.S.
        input = re.sub(r"^[A-Z]\.\w\.","",input)

        # Pronounce_1 the They, Them, their, there, this, that
        input = re.sub(r"(THE\b|The\b|the\b)|(Them\b|them\b)|(They\b|they\b)|(Their\b|their\b)|(There\b|there\b)|(This\b|\bthis\b)|(That\b|\bthat\b)|(Were\b|\bwere\b)|(FROM\b|From\b|\bfrom\b)","",input)

        # Pronounce_2 He, Him, His, Her, she
        input = re.sub(r"(^He\b|^he\b)|(^Him\b|^him\b|^himself\b)|(^His\b|^his\b)|(^Her\b|^her\b|^herself\b)","",input)

        # Auxiliary verbs
        input = re.sub(r"(Could\b|could\b)|(Would\b|would\b)|(Should\b|should\b)","",input)

        # Remove Website references
        input = re.sub(r"(w+w.\w*.\w*.\b)","",input)

        # Remove roman alphabets
        input = re.sub(r"(X.|\bIV.|(I+I+).|IX.|XIV.|VI.|V.)","",input)#Unable to remove all
    
        break
    # Creating regex.txt
    dict_write = codecs.open('regex.txt','w',encoding='utf-8')
    for word in input:
        dict_write.write("%s" % word)
    # Reading the regex file    
    regex_file = 'regex.txt'
    with io.open(regex_file,'r', encoding='utf8') as f: file = f.read()

#getting the newly created regex file
regex_file = file

def normalize_text(input):

    # Taking newly created regex.txt as an input
    input = regex_file
    # Lowercaing the words
    input = input.lower()
    # Eliminating punctuation
    input = input.translate(input.maketrans('', '',string.punctuation))
    # Discarding white space
    input = re.sub(r'[^\w\s]','', input)
    # Removeing number
    input = re.sub(r'\d+','',input)
    # Getting rid of _ before and after words
    input = re.sub(r'(_)','',input)

    # To split the string into list
    words = input.split()
    # Creating an empty list named dictionary to store words
    dict = []
    # Storing only unique words from file into the list
    for word in words:
        # If the current word is not in the dictionary
        if word not in dict:
            # Add it to the end of the list
            dict.append(word)
    
        # Alphabetical order
        dict.sort()

    # Creating dictionary.txt
    dict_write = codecs.open('dictionary.txt','w',encoding='utf-8')
    for word in dict:
        dict_write.write("%s\n" % word)

def main():
    # Function call
    process_regex(readed_file)
    # Function call
    normalize_text(regex_file)

if __name__ == '__main__':
    main()
