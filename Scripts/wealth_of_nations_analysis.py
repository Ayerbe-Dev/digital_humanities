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
smith_fileid = texts.fileids()[1]
smith_text = texts.raw(smith_fileid).lower()
smith_tokens = word_tokenize(smith_text)
smith_words = [""]
smith_rate = [0]
smith_common_words = [""] * 10
smith_highest_rate = [0] * 10
word_index = 0

smith_tokens = [token for token in smith_tokens if not token in stopwords.words('english')]
smith_tokens = [token for token in smith_tokens if token.isalpha()]

def filter_words(word): #quick function to get rid of words like and, or, etc.
    for num in range(0, smith_tokens.count(word)):
        smith_tokens.remove(word)

#check every word in the text
for token in smith_tokens:
    #for each word, compare with all of the words marked down
    word_index = 0 #keep track of the index of the list we're looking at, so we can tell when we reach the end of the list
    for word in smith_words:
        if word == token: #if the word has already been recorded, increase the frequency by 1
            smith_rate[word_index] += 1
            break
        else:
            if word_index == len(smith_words) - 1: 
                #if we make it to the end of our recorded words with no match, add an entry and set the frequency to 1 by default
                smith_words.append(token)
                smith_rate.append(1)
                break
        word_index += 1

word_index = 0

for rate in smith_rate:
    for num in range(0,10):
        if rate > smith_highest_rate[num]:
           smith_highest_rate.insert(num, rate)
           smith_common_words.insert(num, smith_words[word_index])
           smith_highest_rate.pop(10)
           smith_common_words.pop(10)
           break
    word_index += 1

word_index = 0
for word in smith_common_words:
    print(word, ": ", smith_highest_rate[word_index])
    word_index += 1