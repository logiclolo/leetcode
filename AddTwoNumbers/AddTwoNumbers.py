# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def show(self):
        print "Showing list data:"
        current_node = self
        while current_node is not None:
            print current_node.val, " -> ",
            current_node = current_node.next
        print None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy_node = ListNode(0) 
        curr = dummy_node 
        carry = 0

        while l1 != None or l2 != None or carry > 0:

            if l1 is None:
                add1 = 0 
            else:
                add1 = l1.val

            if l2 is None:
                add2 = 0 
            else:
                add2 = l2.val

            total = add1 + add2 + carry 
            a = total / 10 
            b = total % 10 

            curr.next = ListNode(0)
            curr = curr.next 
            curr.val = b
            carry = a
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy_node.next


if __name__ == '__main__':

    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(2)
    node1.next = node2
    node2.next = node3

    node11 = ListNode(3)
    node12 = ListNode(2)
    node13 = ListNode(2)
    node11.next = node12
    node12.next = node13

    solution = Solution().addTwoNumbers(node1,node11) 
    solution.show()

