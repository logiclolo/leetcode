# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):

        """
        Time complexity: O(n)
        Space complexity: O(1)
        """

        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for i in range(n):
            first = first.next

        while first.next != None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next


    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """

        path = 0
        cur = head
        table = []

        table.append(cur)

        while cur.next != None: 
            path += 1
            cur = cur.next
            table.append(cur)

        remove = (path + 1) - n
        if remove < path and remove != 0: 
            table[remove-1].next = table[remove+1]
        elif remove == 0:
            head = table[0].next 
        else:
            table[remove-1].next = None

        return head


        
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

    def create2(self, n):
        head = None
        prev = None

        for i in range(n):
            cur = ListNode(i)
            
            if i == 0:
                head = cur 

            if prev != None:
                prev.next = cur

            prev = cur

        self.display(head)

        return head

if __name__ == '__main__':

    head = Solution().create2(5)
    print '---------------------'
    result = Solution().removeNthFromEnd(head, 5)
    Solution().display(result)

            


