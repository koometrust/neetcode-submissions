class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        wordCount = defaultdict(list)
        for word in strs:
           sortedW = ''.join(sorted(word)) #why this extra ''.join
           wordCount[sortedW].append(word)
        
        return list(wordCount.values())

                # wordCount[word] = 1 + wordCount.get(word, 0)


        
        

