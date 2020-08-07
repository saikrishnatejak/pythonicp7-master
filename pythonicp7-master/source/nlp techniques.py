import  nltk
from nltk.stem import WordNetLemmatizer # import word lemmatizer
from nltk.tokenize import word_tokenize # import word tokenize
""""
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')
"""
input_data=open('input.txt',"r+") # input the data
data=input_data.read()   # read the data
words=word_tokenize(data)
lemm=WordNetLemmatizer()
for k in words:
    print("Lemmatizor for word "+k+" is "+lemm.lemmatize(k)) # parts of speech and it convert in to base form