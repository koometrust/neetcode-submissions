class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # strs = ["act","pots","tops","cat","stop","hat"]

        # [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        hashAgram = defaultdict(list)

        for word in strs:
                sortedWord = sorted(word)
                sortedWord= "".join(sortedWord)
                hashAgram[sortedWord] = [word] + hashAgram.get(sortedWord, [])

        return list(hashAgram.values())























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


        
        

