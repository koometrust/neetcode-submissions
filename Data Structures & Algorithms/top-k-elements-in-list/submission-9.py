class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #  .

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0) #get a good explanation for this so your not lying

        tuSort = []
        for num , freq in count.items():
            tuSort.append([freq, num])
        tuSort.sort() # the last values will have the highest freq

        res = []
        while len(res) < k:
            res.append(tuSort.pop()[1]) #get a good explanation for this
        return res

