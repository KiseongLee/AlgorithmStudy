# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        sorted_list = []
        for list in lists:
            while list:
                sorted_list.append(list.val)
                list = list.next
        sorted_list = sorted(sorted_list)
        
        dummy = cur = ListNode()
        for i in sorted_list:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next
    

'''
1. 모든 연결리스트의 값을 리스트에 넣는다.

2. 리스트를 정렬한다.

3. 정렬한 리스트로 연결리스트를 만든다.
'''