import os
import re
import itertools
import nltk
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
#from autocorrect import Speller
import pandas as pd

#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')
#spell = Speller(lang='en')
ps = nltk.stem.PorterStemmer()

apostrophe_data = pd.read_csv('/home/akhilnv/Desktop/Live Project/scraping/tets/Web Scraping/external_files/data/apostrophe.csv')
slangs_data = pd.read_csv('/home/akhilnv/Desktop/Live Project/scraping/tets/Web Scraping/external_files/data/slangs.csv')
with open("/home/akhilnv/Desktop/Live Project/scraping/tets/Web Scraping/external_files/data/stopwords.txt",'r') as sw:
    stop_words = sw.read()
stopWords = stop_words.split("\n")
apostrophes = dict(zip(apostrophe_data.Contractions, apostrophe_data.Without))
slangs = dict(zip(slangs_data.short_code, slangs_data.word))

html_tags = re.compile('<.*?>',flags=re.MULTILINE)
urls = re.compile('(http|http|www)\S+',flags=re.MULTILINE)
split_attached = re.compile('[A-Za-z][^A-Z]*')
whitespace = re.compile('\s+')
punctuation = re.compile('[^\w\s]')
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
interjections = str.split("Yuck,Ew,Aw,Ouch,Oh,Ah,Ugh,Phew,Phooey,Yum,Yippee,Ack,Blah,Brr,Eek,Uh-huh,Boo,Hm,Gee,Gosh,Whoa,Yahoo,Bah,Hmph,Yowza,Aha,Gadzooks,Pish,Huzzah,Woot,Gada bing,Zowie,Boo hoo,Drat,Duh,Er,Fooey,Gah,Ha,Ick,Geez,Meh,Mmm,Oof,Pfft,Psst,Tsk tsk,Um,okk,hmm,mmm,yepp,eee,hehehe,hehe,yaa,haa",',')

def text_cleaned(input):
    text = input['text']
    corrector = input['corrector']
    # Removing HTML tags
    text = html_tags.sub(r'', text)
    # Removing URLS
    text = urls.sub(r'', text)
    # removing emoji's
    text = emoji_pattern.sub(r'', text)
    # Removing apostrophes and slangs
    words = text.split(' ')
    text = ' '.join([apostrophes[word] if word in apostrophes else word for word in words])
    words = text.split(' ')
    text = ' '.join([slangs[word] if word in slangs else word for word in words])
    # standardizing words
    text = ''.join(''.join(s)[:2] for _, s in itertools.groupby(text))
    # split attached words
    text = ' '.join(split_attached.findall(text))
    # Lower case
    text = text.lower()
    # Stemming
    words = text.split(' ')
    text = ' '.join([ps.stem(i) for i in words])
    # remove interjection
    words = text.split(' ')
    text = ' '.join([word for word in words if word not in interjections])
    # Spelling correction
    if(corrector == 'True'):
        text = str(TextBlob(text).correct())
    # Removing Stopwords
    words = text.split(' ')
    text = ' '.join([word for word in words if word not in stopWords])
    # Removing whitspaces
    text = whitespace.sub(r' ', text)
    text = text.strip()
    # Removing punctuation
    text = punctuation.sub(r'', text)
    output ={"text":text,"corrector":corrector}
    return output
