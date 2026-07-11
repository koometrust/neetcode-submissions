class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
     #hasmap for frequencies
     #put kv pairs in a list
     #sort the list according to frequencies
     #make results array
     #pop from soter list and put in results list
     #return results
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        toSort = []
        for num, freq in count.items():
            toSort.append([freq,num])
        # toSort.sort() #.sort() modifies the original and returnd non Sorted returns a new list
        newToSort = sorted(toSort)

        res = []
        while len(res) < k:
            res.append(newToSort.pop()[1])
        return res


            
   




