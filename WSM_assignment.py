#Opening the sample text document
f1 = open("D:\\ML_projects\WSM assignment\sample.txt", "r")

# importing required modules 
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 

ps = PorterStemmer()

#Tokenizing the complete text document
words = word_tokenize(f1.read())

punctuations = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

#Removing the punctuations
for w in words:
    if w in punctuations:
        words.remove(w)

#Creating a new file to store the stemmed values
f2 = open("result.txt", "w+")

#Stemming the values
for w in words:
    f2.write(w + " : " + ps.stem(w) + "\n") 

#CLosing the files used in the program
f1.close()
f2.close()

