"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list."""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ##Recursive approach: O(m+n) time and space complexity:
        # if not list1:
        #     return list2
        # elif not list2:
        #     return list1
        #
        # if list1.val<list2.val:
        #     list1.next=self.mergeTwoLists(list1.next,list2)
        #     return list1
        # else:
        #     list2.next=self.mergeTwoLists(list1,list2.next)
        #     return list2

        ##iterative approach: O(m+n) time and O(1) space complexity:
        dummy= ListNode()
        current= dummy

        while list1 and list2:
            if list1.val<list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        if list1:
            current.next=list1
        elif list2:
            current.next=list2

        return dummy.next


