import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        # TRY 1
        s에서 윈도우 사이즈 정해가며 중복되는 것 발견시 뛰어넘기
        예
        ws = 3
        pwwkew 일 때 pww는 w가 2개: 2칸 뛰어넘어서 바로 wke로.
        이때 w의 시작, 끝을 잘 고려해야 할 듯.
        (원래는 pww wwk wke)
        
        -> 일단은 뛰어넘는 거 신경 쓰지 말고 해 보기
        
        abcabcbb
        abc
        abca
        
        # TRY 2
        투 포인터로 진행
        i = 0 부터 시작, i를 첫 기준으로 삼고 collections counter 업데이트하는 방식
        
        [문제점]
        타임아웃, collections counter 업데이트시 매번 O(n) 수행 -> 전체 O(n^3) 수행
        
        # TRY 3
        투 포인터로 진행
        i = 0부터 시작하지만 j를 기준으로 삼고 중복시 i를 움직이는 방식, 중복은 딕셔너리로 파악하기
        
        '''
        # TRY 3
        if len(s) == 0: return 0
        i = 0; j = 0; len_long_substring = 1
        counter = dict()
        while(j<len(s)):
            if i == j:
                counter[s[i]] = 1
            elif s[j] in counter and counter[s[j]] == 1:
                while(s[i] != s[j]):
                    counter[s[i]] -= 1
                    i += 1
                i += 1
            else:
                # print(i, j)
                len_long_substring = max(len_long_substring, j - i + 1)
                counter[s[j]] = 1
            # print(s[j], counter, i, j)
            j += 1
            
        return max(len_long_substring, j - i)
        