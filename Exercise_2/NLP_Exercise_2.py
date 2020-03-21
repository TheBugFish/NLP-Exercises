import nltk
import matplotlib
from nltk.corpus import *

# Exercise 1

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['men', 'women', 'people']
    if w.lower().startswith(target))

# cfd.plot()

# Exercise 2

namesFrequency = nltk.ConditionalFreqDist(
    (fileid, name[0])
    for fileid in names.fileids()
    for name in names.words(fileid))

namesFrequency.plot()

# Exercise 3

# allnounsSynset = wordnet.all_synsets('n')
# allnounsSynset2 = wordnet.all_synsets('n')

# allNouns = [noun for noun in allnounsSynset]
# nounsWithoutHyponyms = [noun.lemmas()
#                        for noun in allnounsSynset2 if len(noun.lemmas()) == 1]
#

# print((len(nounsWithoutHyponyms) / len(allNouns)) * 100)

# Exercise 4


def supergloss(s):
    hyponyms = s.hyponyms()
    hypernyms = s.hypernyms()
    hyperNymDefs = [hypernym.definition() for hypernym in hypernyms]
    hyponymDefs = [hyponym.definition() for hyponym in hyponyms]
    return s.definition() + ' '.join(hyperNymDefs) + ' '.join(hyponymDefs)


# print(supergloss(wordnet.synset('car.n.01')))

# Exercise 5


def getWordsByCount(count):
    allWords = [w.lower() for w in brown.words()]
    wordCountDist = nltk.FreqDist(allWords)
    wordsWithCountGreater = [
        word for word in wordCountDist if wordCountDist[word] >= count]
    return wordsWithCountGreater


# print(getWordsByCount(200))

# Exercise 6
# categories = brown.categories()
# for genre in categories:
#    words = brown.words(categories=genre)
#    print(genre + ': ' + str(len(set(words)) / len(words)))

# Exercise 7


# def mostFrequentWords(text):
#    stopwords = nltk.corpus.stopwords.words('english')
#    notStopWords = [word for word in text if word.lower() not in stopwords]
#    freqDist = nltk.FreqDist(notStopWords)
#    return freqDist.most_common(50)


# print(mostFrequentWords(brown.words(categories="news")))

# Exercise 8


# def mostFrequentBigrams(text):
#    stopwords = nltk.corpus.stopwords.words('english')
#    bigrams = nltk.bigrams(text)
#    bigramsWithoutStopwords = [
#        bigram for bigram in bigrams if any(stopwords) not in bigram]
#    freqDist = nltk.FreqDist(bigramsWithoutStopwords)
#    return freqDist.most_common(50)


# print(mostFrequentBigrams(brown.words(categories="news")))

# Exercise 9

def word_freq(word, genre):
    fd = nltk.FreqDist(brown.words(categories=genre))
    return fd[word]


print(word_freq("love", "news"))

# Exercise 10


def find_language(string):
    latin1Languages = [language for language in udhr.fileids()
                       if language.endswith("-Latin1")]
    return [language for language in latin1Languages if string in udhr.words(language)]


print(find_language("basis"))

# Exercise 11

hyponyms_count = 0
hyponyms_sum = 0
for synset in wordnet.all_synsets('n'):
    hyponyms = synset.hyponyms()
    if len(hyponyms) > 0:
        hyponyms_count = hyponyms_count + 1
        hyponyms_sum = hyponyms_sum + len(hyponyms)

print(hyponyms_sum / hyponyms_count)
