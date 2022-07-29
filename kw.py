from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
import nltk


stopWords = set(stopwords.words("english"))
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def hasDigit(word):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for letters in word:
        if(letters in numbers):
            return 0
    return 1

def scrabble_score(word):
    total = []
    for letter in word:
        if letter in score:
            total.append(score[letter.lower()])
    return sum(total)


def getKeyword(sentence):
    sentence_scrabble_scores = dict()
    sentenceWords = word_tokenize(sentence)
    for W in sentenceWords:
        if(hasDigit(W)):
            sentence_scrabble_scores[W] = scrabble_score(W)
    val = []

    sorted_by_value = sorted(sentence_scrabble_scores.items(), key=lambda kv: kv[1])

    if(len(sorted_by_value)>=3):
        for i in range(3):
            (finalKey, finalValue) =  sorted_by_value[len(sorted_by_value)-i-1]
            val += [finalKey]
    return val


def stopWordRemover(text2):
    stemmer = SnowballStemmer("english")
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text2)

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue

        word = stemmer.stem(word)

        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    summary = []
    for key in freqTable.keys():
        summary += [key]
    return summary

def nltk_keyword_find(sentence):
    word_list = nltk.pos_tag(word_tokenize(sentence))
    nouns = []
    prop_nouns = []
    verbs = []
    noStopVerbs = []
    adjectives = []
    for (a,b) in word_list:
        if(b == "NNS" or b == "NN"):
            nouns += [a]
        if(b=="NNPS" or b=="NNP"):
            prop_nouns += [a]
        if(b == "VB" or b=="VBG" or b == "VBD" or b=="VBN" or b=="VBZ" or b=="VBP"):
            verbs += [a]
        if(b == "JJR" or b == "JJS" or b=="JJ"):
            adjectives.append(a)
    for verb in verbs:
        if verb in stopWords:
            continue
        else:
            noStopVerbs.append(verb)
    adjective = ""
    nostopnouns = ""
    for adj in adjectives:
        adjective = adjective + str(adj) + " "
    for adj in nouns:
        nostopnouns = nostopnouns + str(adj) + " "

    
    finalString = ""
    for noun in prop_nouns:
        finalString = finalString + noun + " "
    for noun in getKeyword(nostopnouns):
        finalString = finalString + noun + " "
    for verb in noStopVerbs:
        finalString = finalString + verb + " "
    for verb in getKeyword(adjective):
        finalString = finalString + verb + " "

    stringList = finalString.split(" ")
    finalString = ""
    for T in stringList[:5]:
        finalString = finalString + T + " "
    return finalString