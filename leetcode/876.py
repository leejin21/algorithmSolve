# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        투포인터..
        
        2개 갈 때 한개 간다.
        p1: ', p2: "
        
        '"1 2 3 4 5
        1 '2 "3 4 5
        1 2 '3 4 "5
        
        p2가 더 이상 갈 때가 없으면 p1은 아예 가지 말고 break
        그때의 p1이 정답이 됨.
        
        (반례)
        '"1 2 3 4 5 6
        1 '2 "3 4 5 6
        1 2 '3 4 "5 6
        1 2 3 '4 5 6 "
        
        p2가 2개 중 한개만 가더라도 p1은 1번 더 가고 return 해 주면 됨.
        '''
        # 32ms
        p1 = head; p2 = head
        while(True):
            # p2가 2개 감
            # p1이 1개 감
            p2 = p2.next
            if not p2:
                break
            p2 = p2.next
            p1 = p1.next
            if not p2:
                break
        return p1
            