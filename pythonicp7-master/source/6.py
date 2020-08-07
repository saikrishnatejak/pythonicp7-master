from nltk.util import trigrams # import tridiagrams
from nltk.tokenize import word_tokenize   # import word tokenize
input=open('input.txt','r')
line =input.read()
token= word_tokenize(line)
for x in trigrams(token):
    print(x)