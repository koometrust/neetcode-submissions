class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # start with base case /
        # [1,2,2,3,3,3]//
        #hashmap for counting //
        #sort the pairs in the hash map//
        #store them in an empty array//
        #pop the elemnts in this new array K times//
        #return K//
        #errors

        if not nums:
            return 0

        counter = {}

        for num in nums: #

            counter[num] = 1 + counter.get(num, 0)
        
        hashList = []
        for num, freq in counter.items():
            hashList.append([freq,num])
        hashList.sort()

        final = []
        while len(final) < k:
            final.append(hashList.pop()[1])

        return final

        # Your Output:


        # [1,1]
        # Expected output:


        # [3,2]









        

            


        



















        # count = {}
        # for num in nums:
        #     #store as num,freq
        #     count[num] = 1 + count.get(num,0)

        # toSort = []
        # for num, freq in count.items():
        #     toSort.append([freq,num])
        # toSort.sort()

        # res = []
        # while len(res) < k:
        #  res.append(toSort.pop()[1])

        # return res