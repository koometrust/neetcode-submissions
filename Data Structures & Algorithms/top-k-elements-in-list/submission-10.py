class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        #sort the nums and frequencys
        sorted = []
        for num, freq in count.items():
            sorted.append([freq, num])
        sorted.sort()

        res = []
        while len(res) < k:
            res.append(sorted.pop()[1])
        return res
