class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        romantable = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }

        value = 0
        pre = 0

        for ss in s:
            cur = romantable[ss]

            if cur > pre:
                value = value + cur - pre - pre
            else:
                value = value + cur
            
            pre = cur

        return value

if __name__ == '__main__':

    s = 'XIX'
    s = 'LXIII'
    s = 'CC'

    print Solution().romanToInt(s) 

