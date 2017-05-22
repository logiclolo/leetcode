class Solution(object):
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """

        length = len(string)
        pos = True
        i = 0
        div = 1
        result = 0 
        digit_flag = False 
        while i < length:
            value = ord(string[i])
            if self.isDigit(value):
                result = result * 10 + value - 48
                digit_flag = True
            elif value == 32 and digit_flag is False: # space
                None
            elif value == 45: # minus 
                pos = False
                if i + 1 < length and not self.isDigit(ord(string[i+1])):
                    return 0
            elif value == 43: # plus
                pos = True
                if i + 1 < length and not self.isDigit(ord(string[i+1])):
                    return 0
            else:
                break

            i = i + 1
            

        if pos:
            if result > 2147483647:
                return 2147483647
            else:
                return result 
        else:
            if -result < -2147483648:
                return -2147483648 
            else:
                return -result

    def isDigit(self, value):
        if value >= 48 and value <= 57:
            return True
        else:
            return False


if __name__ == '__main__':

    s = 'sdfs-2147483649sdfsdf'
    s = "+--2"
    s = '  +0 123'

    obj = Solution()
    print obj.myAtoi(s)
