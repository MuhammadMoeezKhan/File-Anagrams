#Run Command: python3 solution.py < adventures_of_huckleberry_finn.txt > output.txt

import re
from collections import defaultdict
from collections import Counter

anagramInformation = [None] * 2

def processText(text):
    cleaned_text = re.sub(r'[!?-_ˆ,*;∑:.\[\]\(\)"\'\d]', '', text)
    words = [word for word in re.split(r'\s+', cleaned_text) if word]
    return words


def findAnagramsAndFrequency(fileContent):
    anagramDict = defaultdict(set)
    anagramFreq = defaultdict(int)

    for word in fileContent:
        lowerWord = word.lower()
        freqChar = [0] * 256
        for char in lowerWord:
            freqChar[ord(char)] += 1
        anagramDict[tuple(freqChar)].add(word)
        anagramFreq[tuple(freqChar)] += 1

    anagramInformation[0], anagramInformation[1] = anagramDict, anagramFreq

    with open("output.txt", "w") as outputFile:
        print("Anagram Finder", file=outputFile)
        print("{:<15} {:<10}".format("Anagrams", "Frequency"), file=outputFile)

        for freqChar, words in anagramDict.items():
            if len(words) > 1:
                print("{:<15} {:<10}".format(', '.join(words), anagramFreq[freqChar]), file=outputFile)

def search(searchWord):
    lowerWord = searchWord.lower()
    freqChar = [0] * 256
    for char in lowerWord:
        freqChar[ord(char)] += 1
    
    anagramDict, anagramFreq = anagramInformation

    if freqChar in anagramDict:
            print(searchWord + " Anagrams: " + list(anagramDict[freqChar]) + " Frequencies: " + anagramFreq[freqChar])
    else:
        print("string not found")
    

def writeResultToOutputFile():
    with open('adventures_of_huckleberry_finn.txt', 'r') as file:
        fileContent = file.read()
    processedFile = processText(fileContent)
    print(processedFile)
    findAnagramsAndFrequency(processedFile)

writeResultToOutputFile()