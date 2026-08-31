class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # hashAgram = defaultdict(list)

        # for word in strs:
        #         sortedWord = sorted(word)
        #         sortedWord= "".join(sortedWord)
        #         # hashAgram[sortedWord] = word + hashAgram.get(sortedWord, "")

        #         hashAgram[sortedWord] = [word] + hashAgram.get(sortedWord, [])


        # return list(hashAgram.values())

        freqArrayHash = defaultdict(list)

        for word in strs:
            count = [0] * 26 

            for character in word:
                count[ord(character)- ord('a')] += 1 #increment 0 by one
            freqArrayHash[tuple(count)].append(word)

        return list(freqArrayHash.values())
            



        




























        # anagrams = defaultdict(list)


        # for word in strs:
        #         newWord = ''.join(sorted(word))
        #         # anagrams[newWord].append(word)
        #         anagrams[newWord] = [word] + anagrams.get(newWord, [])


        # return list(anagrams.values())

        # # wordCount = defaultdict(list)
        # # for word in strs:
        # #    sortedW = ''.join(sorted(word)) #why this extra ''.join
        # #    wordCount[sortedW].append(word)
        
        # # return list(wordCount.values())

        #         # wordCount[word] = 1 + wordCount.get(word, 0)


        
        

