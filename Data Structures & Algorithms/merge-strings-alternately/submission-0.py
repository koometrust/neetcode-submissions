class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Input: word1 = "abc", word2 = "xyz"
                        #   |              |
        # Output: "axbycz"
        word3 = ''
        pointerOne, pointerTwo = 0, 0

        while pointerOne < len(word1) and pointerTwo < len(word2): 
            word3 += word1[pointerOne]
            word3 += word2[pointerTwo]
            pointerOne +=1
            pointerTwo +=1

        #if word 2 0r 1 remains
        #slicing ni noma
        if len(word1) > pointerOne:
            word3 += word1[pointerOne: ]

        if len(word2) > pointerTwo:
            word3 += word2[pointerTwo: ]
        

        return word3





        # for letter in word1:
        #     # word3.add(letter)
        #     # word3 = ''.join(letter)
        #     word3 += letter

        # for letter in word2:
        #     # word3.add(letter)
        #     # word3 = ''.join(letter)
        #     word3 += letter




        # if word1:
        #     for letter in word1:
        #         word3 = ''.join(letter)
        # if word2:
        #     for letter in word2:
        #         word3 = ''.join(letter)


        return word3


        