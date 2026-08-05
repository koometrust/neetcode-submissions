class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            #store as num,freq
            count[num] = 1 + count.get(num,0)

        toSort = []
        for num, freq in count.items():
            toSort.append([freq,num])
        toSort.sort()

        res = []
        while len(res) < k:
         res.append(toSort.pop()[1])

        return res