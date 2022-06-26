import numpy as np
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pymongo
client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.nhkcllc.mongodb.net/test")
db = client["data"]
mycllection = db["data"]

all_rec = mycllection.find()

for row in all_rec:
    print(row)

all_rec = mycllection.find()
list_a = list(all_rec)
df = pd.DataFrame(list_a)




#%%
from nltk.corpus import stopwords
print(set(stopwords.words('english')))

stop = stopwords.words('english')
# Set of stopwords to remove
stop = set(stop)

# Set of punctuation signs to remove
from string import punctuation

def lower(text):
    return text.lower()

def remove_punctuation(text):
    return text.translate(str.maketrans('','', punctuation))


#Join the list of strings into a string based on delimiter ('')
def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in stop])

import re #re — Regular expression operations

# Removing all words with digits and standalone digits
def remove_digits(text):
    return re.sub(r'\d+', '', text)

# One function to clean it all
def clean_text(text):
    text = lower(text)
    text = remove_punctuation(text)
    text = remove_stopwords(text)
    text = remove_digits(text)
    return text

df['all1_clean']=df['Description'].apply(clean_text)

vectorizer = TfidfVectorizer(analyzer='word', lowercase=False)
X = vectorizer.fit_transform(df['all1_clean'])
tag_vectors = X.toarray()


#%%
