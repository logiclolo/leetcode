class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False
            
        div = 1

        while x/div >= 10:
           div = div * 10 
        
        while x > 0:
            digit = x / div
            if digit != x % 10:
                return False
            x = (x % div) / 10
            div = div / 100
            print 'digit is %d' % digit
            print 'x is %d' % x

        return True



if __name__ == '__main__':

    x = -1234
    x = 8888888888888888
    x = 23212232
    x = 102201
    x = 1000021
    # x = -214748364
    # x = -432

    print Solution().isPalindrome(x)
