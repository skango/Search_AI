import selenium
from bs4 import BeautifulSoup
import requests


def testfunction():
    print("This is a test!")
    print(selenium.__file__)
    r = requests.get("https://skangogames.com")
    print(r.status_code)
    rawData = r.text
    print(rawData)
    soup = BeautifulSoup(rawData,"html.parser")
    print("Soup Sucessfully created!")

testfunction()