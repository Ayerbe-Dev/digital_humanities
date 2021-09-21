# imports
import nltk
from nltk import word_tokenize
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#from sklearn.feature_extraction.text import TfidfVectorizer

#set up the corpuses
texts = PlaintextCorpusReader('./texts/', '.*\.txt')
gibbon_fileid = texts.fileids()[0]
gibbon_text = texts.raw(gibbon_fileid).lower()
gibbon_tokens = word_tokenize(gibbon_text)
gibbon_words = [""]
gibbon_rate = [0]
gibbon_common_words = [""] * 10
gibbon_highest_rate = [0] * 10
word_index = 0

gibbon_tokens = [token for token in gibbon_tokens if not token in stopwords.words('english')]
gibbon_tokens = [token for token in gibbon_tokens if token.isalpha()]

def filter_words(word): #quick function to get rid of words like and, or, etc.
    for num in range(0, gibbon_tokens.count(word)):
        gibbon_tokens.remove(word)

#check every word in the text
for token in gibbon_tokens:
    #for each word, compare with all of the words marked down
    word_index = 0 #keep track of the index of the list we're looking at, so we can tell when we reach the end of the list
    for word in gibbon_words:
        if word == token: #if the word has already been recorded, increase the frequency by 1
            gibbon_rate[word_index] += 1
            break
        else:
            if word_index == len(gibbon_words) - 1: 
                #if we make it to the end of our recorded words with no match, add an entry and set the frequency to 1 by default
                gibbon_words.append(token)
                gibbon_rate.append(1)
                break
        word_index += 1

word_index = 0

for rate in gibbon_rate:
    for num in range(0,10):
        if rate > gibbon_highest_rate[num]:
           gibbon_highest_rate.insert(num, rate)
           gibbon_common_words.insert(num, gibbon_words[word_index])
           gibbon_highest_rate.pop(10)
           gibbon_common_words.pop(10)
           break
    word_index += 1

word_index = 0
for word in gibbon_common_words:
    print(word, ": ", gibbon_highest_rate[word_index])
    word_index += 1