class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x < 0:
            neg = True
            x = -x
        else:
            neg = False

        string = str(x)
        l = len(string)
        digits = ''

        for i in range(l):
            digits = digits + string[l-(i+1)] 

        value = int(digits)

        if neg == False and value > 2147483647:
            return 0
        elif neg == True and value > 2147483648:  
            return 0
        elif neg == True:
            return -value
        else:
            return value 

    def reverse1(self, x):

        # integer type in Python is 64bits
        # so don't worry it will overflow and is able to check the overflow of 32bits integer 
        val = 0
        if x >= 0:
            while x:
                val = val * 10 + x % 10
                x = x / 10
        else:
            while x:
                print x
                val = val * 10 - (10 - (x % 10))
                x = (x / 10) + 1

        if val > 2147483647: 
            return 0
        elif val < -2147483648:
            return 0
        else:
            return val
            


if __name__ == '__main__':

    x = -1234
    x = 8888888888888888
    x = 2147483647 
    x = -8463847413
    # x = -214748364
    # x = -432

    print Solution().reverse1(x)
        
