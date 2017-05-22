# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        cur = dummy

        while True:
            if l1 != None and l2 != None:
                if l1.val < l2.val:
                    cur.next = l1
                    cur = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    cur = l2
                    l2 = l2.next

            elif l2 == None:
                cur.next = l1 
                return dummy.next

            elif l1 == None:
                cur.next = l2
                return dummy.next

            else:
                return dummy.next

    def display(self, head):

        if head is None:
            print 'Empty linked-list'
            return
        
        while True:
            print head.val
            print '->'
            if head.next == None:
                break
            head = head.next

    def create(self, n):

        head = ListNode(None) 
        cur = head
        for i in range(n):
            cur.val = i
            if i != (n-1):
                cur.next = ListNode(None)
                cur = cur.next
        self.display(head)

        return head


if __name__ == '__main__':

    head = Solution().create(5)
    head2 = Solution().create(19)
    print '---------------------'
    result = Solution().mergeTwoLists(head, head2)
    Solution().display(result)
        
