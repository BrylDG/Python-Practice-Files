from itertools import zip_longest

word1 = input()
word2 = input()

print(word1)
print(word2)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        # Iterate while EITHER word has letters left
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        print ("".join(result))


Solution().mergeAlternately(word1, word2)