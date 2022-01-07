# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 24ms
        '''
        use stack
        <예외 1> [미완]
        [1,2,3], n = 3
        => head를 2로 바꿔줘야 함.
        
        <예외 2> [완]
        [1,2,3], n = 1
        => 2.next를 None으로 바꿔줘야 함.
        
        '''
        
        nodeList = []
        temp = head
        
        while(temp):
            nodeList.append(temp)
            temp = temp.next
            
        if len(nodeList) > n:
            
            prevNode = nodeList[-1*n-1]
            nextNode = nodeList[-1*n+1] if n>1 else None
                # 예외 2
            
            prevNode.next = nextNode
            
        else:
            # 예외 1
            head = head.next

        return head
        