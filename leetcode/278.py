# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

import sys
sys.setrecursionlimit(10000)

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer = [0]
        if n==1: return 1
        
        def binSearch(l, r):
            # print(l, r)
            m = (r-l)//2+l
            
            if l==m and isBadVersion(m+1): 
                answer[0] = l+1
                return
            elif l>r:
                return
            
            if not isBadVersion(m+1):
                binSearch(m+1, r)
            else:
                binSearch(l, m)
        binSearch(0, n-1)
        
        return answer[0]