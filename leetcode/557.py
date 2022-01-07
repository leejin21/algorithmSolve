class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        # 59ms
        sSplitted = s.split(' ')
        sSplitted = [word[::-1] for word in sSplitted]
        return ' '.join(sSplitted)
        
        # 155ms
#         newSentence = []
#         for word in s.split(' '):
#             reversedWord = [c for c in word]
#             for i in range(len(reversedWord)//2):
#                 reversedWord[i], reversedWord[-i-1] = reversedWord[-i-1], reversedWord[i]
#             newSentence.append(''.join(reversedWord))
        
#         # print(newSentence)
#         return ' '.join(newSentence)