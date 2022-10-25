import selenium
from bs4 import BeautifulSoup
import requests
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

# def testfunction():
#     print("This is a test!")
#     print(selenium.__file__)
#     r = requests.get("https://skangogames.com")
#     print(r.status_code)
#     rawData = r.text
#     print(rawData)
#     soup = BeautifulSoup(rawData,"html.parser")
#     print("Soup Sucessfully created!")
#
# testfunction()

#nltk.download('punkt')
#nltk.download('stopwords')
stemmer = PorterStemmer()

# Clean text and leave only useful Keywords -- https://monkeylearn.com/topic-analysis/
def process_text(text):
    # Make all the strings lowercase and remove non alphabetic characters
    text = re.sub('[^A-Za-z]', ' ', text.lower())

    # Tokenize the text; this is, separate every sentence into a list of words
    # Since the text is already split into sentences you don't have to call sent_tokenize
    tokenized_text = word_tokenize(text)

    # Remove the stopwords and stem each word to its root
    clean_text = [
        stemmer.stem(word) for word in tokenized_text
        if word not in stopwords.words('english')
    ]

    # Remember, this final output is a list of words
    return clean_text

def CountWords(x):
    Words = []
    Count = []
    for i, v in enumerate(x):
        Words.append(v)
        matchcount = 0
        for j in x:
            if (v == j):
                matchcount += 1
            else:
                pass
                #print("No Match")

        Count.append(matchcount)

    #print(Words)
    #print(Count)

    #print(sorted(Count, reverse=True))
    IndexSort = sorted(range(len(Count)), key=lambda k: Count[k],reverse=True)
    WordsSortedByCriteria = []
    for i, v in enumerate(IndexSort):
        print(Words[IndexSort[i]], "Gameorda ", Count[IndexSort[i]])
        if (Words[IndexSort[i]] in WordsSortedByCriteria):
            pass
        else:
            WordsSortedByCriteria.append(Words[IndexSort[i]])

    return WordsSortedByCriteria

Text = input("Enter Text: ")
print(CountWords(process_text(Text)))
print(process_text(Text))
#Get most important topics: https://www.toptal.com/python/topic-modeling-python
