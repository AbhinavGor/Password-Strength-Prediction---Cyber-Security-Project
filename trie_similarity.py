import errno

from trietree import TrieTree
from itertools import groupby
from array import array
from itertools import islice
import sys

from  dfflb import difflibScore


VOWELS = 'aeiou'
NO_SUGGESTION = 'NO_SUGGESTION'

class SpellChecker(object):
    """
    Spell checker class. On init it will read /usr/share/dict/words. The method correct will offer a correction.
    A good improvement would be to teach the tree which are the most common words, and choose based on ocurrence instead
    of picking the first valid candidate, but that's out of the scope of the exercise. Other possible optimization is 
    multithreaded generation of combinations and discard of prefixes.
    """
    trie = TrieTree()

    def __init__(self):
        """Reads the file and generates the trie tree"""
        file = open('smallsample.txt')
        for word in file:
            self.trie.addWord(str.strip(str.lower(word)))


    def correct(self, word):
        """Tries to correct a given word. The selected correction will be the first to be a valid english word"""

        #Try with lower case first
        word = str.lower(word)
        if self.trie.containsWord(word):
            return word

        #Generate tuples with the different splits based on duplicated consonant
        duplicates = self._split_duplicates(word)

        

        cprefixes = []

        #Generate combinations and check the build prefixes to see if they exist in the trie tree. This will allow us
        #to get rid of a lot of invalid roots early on. Everytime we check a prefix we get the subtree of the possible
        #combinations for that prefix with other sufixes.

        for prefixes in duplicates:
            combinations = []
            for prefix in prefixes:
                shuffledList = self._shuffleVowels(prefix)
                if len(cprefixes) > 0:
                    combinations += [ (pref+suftuple[0], suftuple[1]) for pref, tree in cprefixes for suftuple in self._check_suffix(tree,shuffledList) if suftuple]
                else:
                    combinations += [shuffledPrefix for shuffledPrefix in self._check_suffix(self.trie,shuffledList) if shuffledPrefix]
            #Use only one copy of each
            cprefixes = set(combinations)
            

        for dword,tree in cprefixes:
            if self.trie.containsWord(dword):
                return dword

        return NO_SUGGESTION

    def _check_suffix(self, tree, words):
        for word in words:
            yield tree.containsPrefix(word)

    def _split_duplicates(self, word):
        """
        Will generate a series of prefixes on duplicated consonant. For example adddress would be split in ((ad,add)
        ,(r,rr),(es,ess))
        """
        sflist = []
        index = 0

        wlen = len(word)

        for name, group in groupby(word):
            size = len(list(group))
            if size > 1:

                #There are no words with more than three repeated characters
                if size > 2:
                    sflist.append((word[:index+1], word[:index + 2], word[:index+3]))
                else:
                    sflist.append((word[:index+1], word[:index + 2]))


                if index + size != wlen:
                    sflist += self._split_duplicates(word[index+size:])

                break


            index += size

        if not sflist:
            sflist.append((word,))

        return sflist

    def _shuffleVowels(self, word):
        """
        Will generate combinations of the same word with the vowels changed, and then generate possible combinations
        if vowels are repeated.
        """
        wordList = []
        wordList.append(word)

        positions = []

        corrections = [word]

        for x,c in enumerate(word):
            if c in VOWELS:
                positions.append(x)

        for index in positions:

            for word in islice(wordList,0, len(wordList)):
                for bowel in VOWELS:
                    if word[index] != bowel:
                        copy = word.split()
                        copy.append("c")
                        copy[index] = bowel
                        strcopy = ''.join(copy)

                        wordList.append(copy)

                        #For every combination try and remove duplicates vowels that might have been created
                        corrections += self._remove_duplicated_vowels(strcopy)


        return set(corrections)


    def _remove_duplicated_vowels(self,word):
        """Will generate a list of all possible combinations of removed duplicated vowels"""
        index = 0

        listWords = [word]

        for name, group in groupby(word):
            size = len(list(group))
            if size > 1 and name in VOWELS:
                dword = word[0:index] + word[index+1:]
                listWords.append(dword)
                listWords += self._remove_duplicated_vowels(dword)

            index += size

        return set(listWords)




if __name__ == '__main__':
    sc = SpellChecker()
    for word in sys.stdin:
        word = str.strip(word)

        correction = sc.correct(word)
        print(correction)
        print(difflibScore(word))
        if correction is NO_SUGGESTION:
            sys.exit(-1)
