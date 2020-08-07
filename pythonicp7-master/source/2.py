from nltk.stem import SnowballStemmer # import snowball stemmer
input_data=open('input.txt',"r+")
data=input_data.read() # read the data
words=data.split("\n")
words=data.split(" ")
stemm=SnowballStemmer('english') # here we used english languaghe
for k in words:
  print("Stemmimg for word "+k+" is "+ stemm.stem(k)) # convert it in to base forrm.