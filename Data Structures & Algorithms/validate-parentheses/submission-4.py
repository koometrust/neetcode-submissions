class Solution:
    def isValid(self, s: str) -> bool:
        #{} [] ()

        #)-( }-{ ]-[


        hash = {

            ")": "(",
            "}": "{",
            "]": "[",

        }
        

        # "{}[]()"

        parList = []

        # for c in s:
        #     if c in hash: #gets the keys()
        #         parList.append(c)
        #     else:
        #         if s[c-1] == hash[c]:
        #             parList.pop()
            
        # while  parList:
        #     return False
        # return True


        for c in s:
            if c in hash.values(): #gets the values()
                parList.append(c)
            else:
                if c in hash:
                    if parList and parList[-1] == hash[c]:
                        parList.pop()
                    else:
                        return False
            
        while  parList:
            return False
        return True






        # s="[({])}"

        