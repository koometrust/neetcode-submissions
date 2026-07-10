class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap to see if we've seen this character before then increment it's counter
        # #Keys will char count and value will be the anagrams
        # # 0 - 26
        # groupAnagram = defaultdict(list)
        # for s in strs:
            
        #     count = [0] * 26 # a ... initalized as 0 so we will increment those slots. Question? what Data structure is count is it a list of [0]'s
        #     for l in s:
        #         count[ord(l) - ord("a")] += 1 # then explain the [ord(l) - ord("a")] does it go into our count which has 26 [0] spaces then finds that exact space and increments it by 1
            
        #     groupAnagram[tuple(count)].append(s) #Kindly explain  why it is not the traditional groupedAngram[count] = s . Additionally We turn count to a tuple because they are immutable
        
        # return list(groupAnagram.values() #TypeError: Your output was <class 'dict_values'>, but the expected return type is List[List[str]]. SO YOU CONVERT IT TO A LIST
        #
        #
        #

        #
        #

        # .
        # ..
        # .
        # .
        # .
        # JUDES SORTED ANSWER WE ARE STILL CHECKING AMAZING JUDE
        hashy = defaultdict(list)
        for str in strs:
            sortedStr = tuple(sorted(str))
            hashy[sortedStr].append(str)

        return list(hashy.values())

