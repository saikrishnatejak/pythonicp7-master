from nltk.tokenize import word_tokenize # this for separating the words
from nltk.stem import SnowballStemmer
input_data=open('input.txt',"r+")
data=input_data.read()
print("Tokenization: ",word_tokenize(data)) # print the words
