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

        # toSort = []
        # for num, freq in count.items():
        #     toSort.append([freq,num])
        # toSort.sort() #.sort() modifies the original and returnd non Sorted returns a new 

        # res = []
        # while len(res) < k:
        #     res.append(toSort.pop()[1])
        # return res

#Using a Heap (min-heap)
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for num in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
    

            
   




