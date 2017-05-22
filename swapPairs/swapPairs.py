# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head 
        cur = dummy 

        while cur.next != None:
            if cur.next.next != None:
                tmp = cur.next
                tmp1 = cur.next.next
                tmp2 = cur.next.next.next

                cur.next = tmp1 
                tmp1.next = tmp
                tmp.next = tmp2
            else:
                break

            cur = cur.next.next
                

        return dummy.next

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

if __name__ == '__main__':

    head = Solution().create2(6)
    print '---------------------'
    result = Solution().swapPairs(head)
    Solution().display(result)
