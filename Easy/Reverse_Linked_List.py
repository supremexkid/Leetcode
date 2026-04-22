# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Constraints:
#
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# https://leetcode.com/problems/reverse-linked-list/description/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        tmp_head = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = tmp_head
            tmp_head = current
            current = next_node

        return tmp_head

def print_list(node):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    print(vals)

head = ListNode(1, ListNode(3, ListNode(5)))
obj = Solution()

reversed_head = obj.reverseList(head)
print_list(reversed_head)  # [5, 3, 1]

back_to_normal = obj.reverseList(reversed_head)
print_list(back_to_normal)  # [1, 3, 5]

