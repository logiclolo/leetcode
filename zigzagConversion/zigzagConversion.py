class Solution(object):
    def convert(self, s, numRows):

        l = len(s)
        row = 0 
        ss = ''
        if numRows == 1:
            return s

        for r in range(numRows):
            stride = 2 * numRows - 2
            stride1 = 2 * (numRows - r) - 2
            stride2 = 2 * (r + 1) - 2
            n = 0
            i = r
            if r == 0 or r == (numRows - 1):
                stride  = 2 * numRows - 2
                while i < l: 
                    ss = ss + s[i]
                    n = n + 1
                    i = i + stride 
            else:
                while i < l: 
                    ss = ss + s[i]
                    if n % 2 == 0:
                        stride = stride1
                    else:
                        stride = stride2
                    n = n + 1
                    i = i + stride 

        return ss


if __name__ == '__main__':

    n = 4 
    s = 'abcdefghijklmnopq'
    # s = "ab"
    print Solution().convert(s, n)
