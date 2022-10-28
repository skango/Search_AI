# import selenium
# from bs4 import BeautifulSoup
# import requests
import re
import nltk
import tkinter
from tkinter import simpledialog
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import GaussianNB
# from sklearn.metrics import classification_report
import Scraper
#from gensim import corpora
#from gensim import models

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

def getWordArray(text):
    # Make all the strings lowercase and remove non alphabetic characters
    text = re.sub('[^A-Za-z]', ' ', text.lower())

    # Tokenize the text; this is, separate every sentence into a list of words
    # Since the text is already split into sentences you don't have to call sent_tokenize
    tokenized_text = word_tokenize(text)
    return tokenized_text

def getWordArrayWithDots(text):
    return text.split()

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
        if (Words[IndexSort[i]] not in WordsSortedByCriteria):
            WordsSortedByCriteria.append(Words[IndexSort[i]])

    return WordsSortedByCriteria

def AnalyzeWhatIsWhat(x):
    for i,v in enumerate(x):
        if (v == "is"):
            if (x[i + 1] == "a" or x[i + 1] == "the"):
                print(x[i - 1], " is", x[i + 2])
            else:
                print(x[i - 1], " is", x[i + 1])

def AnalyzeWhatIsWhat2(x):
    WritingSentence = False
    sentence = []
    for i,v in enumerate(x):
        if (v == "is"):
            WritingSentence = True
            sentence.append(x[i - 1])
            sentence.append(" is ")
            continue
        if ("." in v and WritingSentence):
            sentence.append(x[i])
            WritingSentence = False
            sentencetosay = ""
            for i in sentence:
                sentencetosay += " "
                sentencetosay += i

            print(sentencetosay)
            sentence.clear()
            continue
        if (WritingSentence):
            sentence.append(x[i])


#Text = input("Enter Text: ")
ROOT = tkinter.Tk()
ROOT.withdraw()
# the input dialog
Text = simpledialog.askstring(title="Test",
                                  prompt="Enter Text:")
#print(" Text is ", Text)
if (len(Text) < 500):
    print("\nYou must enter at least 500 Characters! You entered: ", len(Text), "/", " 500")
    exit(-1)

WordsSortyedByCount = CountWords(process_text(Text))

print(WordsSortyedByCount)
WordsSorted = process_text(Text)
print(WordsSorted)
AnalyzeWhatIsWhat2(getWordArrayWithDots(Text))

print("===========================================")
print("===========================================")
print("===========================================")
print("===========================================")
print("===========================================")

if (WordsSortyedByCount[0] != WordsSorted[0]):
    Scraper.GoogleSearch(WordsSortyedByCount[0] + " " + WordsSorted[0])
else:
    Scraper.GoogleSearch(WordsSortyedByCount[0] + " " + WordsSortyedByCount[1])

# matrix = CountVectorizer(max_features=1000)
# vectors = matrix.fit_transform(process_text(Text)).toarray()
# vectors_train, vectors_test, topics_train, topics_test = train_test_split(vectors, getWordArray(Text))
# classifier = GaussianNB()
# classifier.fit(vectors_train, topics_train)
#
#
# topics_pred = classifier.predict(vectors_test)
#
#
#
# #(classification_report(topics_test, topics_pred))


#print(ReverseQuestion(getWordArrayWithDots(Text)))
#Get most important topics: https://www.toptal.com/python/topic-modeling-python