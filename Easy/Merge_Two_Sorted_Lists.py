# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# Example 1:
# Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
# Example3:
# Input: list1 = [], list2 = [0]
# Output: [0]
#
# Constraints:
#
# The number of nodes in both lists is in the range[0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non - decreasing order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        new_node = ListNode(0)
        current_node = new_node

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current_node.next = list1
                list1 = list1.next
                current_node = current_node.next
            else:
                current_node.next = list2
                list2 = list2.next
                current_node = current_node.next
        if list1 is not None:
            current_node.next = list1
        else:
            current_node.next = list2

        return new_node.next

    # def print_list(self, head):
    #     values = []
    #     while head is not None:
    #         values.append(head.val)
    #         head = head.next
    #     print(values)




# list1 = ListNode(1, ListNode(3, ListNode(5)))
# list2 = ListNode(2, ListNode(4, ListNode(6)))
#
# obj = Solution()
# result = obj.mergeTwoLists(list1, list2)
# obj.print_list(result)
# print(result)