class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
   
        """
        sort it for a greedy approach

        """
        people.sort()

        l,r = 0 , len(people) - 1
        boat = 0

        while l <= r:
            sum = people[l] + people[r]

            if sum > limit:
                if people[r] <= limit:
                    boat += 1
                    r -= 1
            else:
                boat += 1
                r-=1
                l+=1


        return boat

            







