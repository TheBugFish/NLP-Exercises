import nltk

# perparation
# nltk.download()

from nltk.book import *


def lexical_diversity(text):
    return (len(set(text)) / len(text))

# Exercise 1


wordCount = len(text2)
distinctWordCount = len(set(text2))
# print(wordCount)
# print(distinctWordCount)
# print(lexical_diversity(text2))

# Exercise 2

#text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"])

# Exercise 3

collocations = text6.collocation_list()
# print(collocations)

# Exercise 4

indexes = text9.index('sunset')
# print(indexes)

# Exercise 5

val1 = len(sorted(set(w.lower() for w in text1)))
# print(val1)
val2 = len(sorted(w.lower() for w in set(text1)))
# print(val2)
# difference is that the first one creates a set of the tolowered words while the second one creates a set of all the words and toloweres them afterwards.
# Capital starting letters might be what makes the difference here.

# Exercise 6

lastTwoWords = text2[len(text2)-2:len(text2)]
# print(lastTwoWords)

# Exercise 7

wordsWithLength4 = [w for w in text6 if len(w) == 4]
wordsLength4FreqDist = FreqDist(wordsWithLength4)

orderedWords = wordsLength4FreqDist.most_common()
print(orderedWords)

# Exercise 8

#textSet = set(text6)
# for word in textSet:
#    if (len(word) > 1) & word[0].isupper():
#        print(word)

# Exercise 9


def findAllWordsByCase(case):
    text6Set = set(text6)
    if(case == "a"):
        return [word for word in text6Set if word.endswith("ing")]
    elif(case == "b"):
        return [word for word in text6Set if "z" in word]
    elif(case == "c"):
        return [word for word in text6Set if "pt" in word]
    else:
        return []


# print(findAllWordsByCase("a"))

# Exercise 10

sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'shore']

print([word for word in sent if word.startswith("sh")])
print([word for word in sent if len(word) > 4])

# Exercise 11

sum(len(w) for w in text1)
# calculates sum of length of all words in text1

# Answer yes!
wordLengthSum = sum(len(w) for w in text1)

averageWordLength = wordLengthSum / len(text1)
print(averageWordLength)

# Exercise 12


def freq(word, text):
    freqDist = FreqDist(text)
    return freqDist[word]


print(freq("promise", text4))
