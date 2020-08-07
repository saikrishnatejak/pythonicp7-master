from nltk import pos_tag,ne_chunk,wordpunct_tokenize # it tells which is an organization ,place or name etc
file1=open('input.txt','r') # Input a file
text =file1.readline()
while text!='':
 print(ne_chunk(pos_tag(wordpunct_tokenize(text))))
 text=file1.readline()