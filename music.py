import requests
import os, random


def get_sentiment(text):
    a = requests.post(url="http://text-processing.com/api/sentiment/", data={"text": text})
    return a.json()['label']


def get_song(text):
    sentiment = get_sentiment(text)

    if sentiment == 'pos':
        return "music/pos/" + random.choice(os.listdir(os.curdir + "/music/pos/"))

    if sentiment == 'neg':
        return "music/neg/" + random.choice(os.listdir(os.curdir + "/music/neg/"))

    return "music/neutral/" + random.choice(os.listdir(os.curdir + "/music/neutral/"))


if __name__ == '__main__':
    print(get_song("nothing"))
