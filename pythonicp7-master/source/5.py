from nltk.tokenize import word_tokenize # this for parts of speech
from nltk import pos_tag, ne_chunk

input = open('input.txt','r', encoding="utf-8")
text = input.read() # read the file
words = word_tokenize(text)
print(ne_chunk(pos_tag(words))) # print according to parts of speech