# Problem: Merge Two Sorted Lists = https://leetcode.com/problems/merge-two-sorted-lists/description/

def mergeTwoLists(list1, list2):
    dummy = ListNode(-1)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1 
            list1 = list1.next
        else:
            current.next = list2    
            list2 = list2.next   
        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next


# mergeTwoLists([1,2,4], [1,3,4])


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(4)

# node1.next = node2
# node2.next = node3

# head = node1

# current = head

# while current != None:
#     print(current.val)
#     current = current.next