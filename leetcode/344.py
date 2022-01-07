class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        
        # 188ms
        for i in range(len(s)//2):
            s[i], s[-1-i] = s[-1-i], s[i]
        
        # 289ms
        # s.reverse()
        
        
        # 376ms
        # for i in range(len(s)//2):
        #     s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]