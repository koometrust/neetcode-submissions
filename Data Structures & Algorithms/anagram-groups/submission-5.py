class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)


        for word in strs:
                newWord = ''.join(sorted(word))
                anagrams[newWord].append(word)

        return list(anagrams.values())

        # wordCount = defaultdict(list)
        # for word in strs:
        #    sortedW = ''.join(sorted(word)) #why this extra ''.join
        #    wordCount[sortedW].append(word)
        
        # return list(wordCount.values())

                # wordCount[word] = 1 + wordCount.get(word, 0)


        
        

