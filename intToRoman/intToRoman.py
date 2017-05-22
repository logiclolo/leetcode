"""
please see the regulation of roman numerals
http://www.geeksforgeeks.org/converting-roman-numerals-decimal-lying-1-3999/
"""
class Solution(object):
    inttable = [1,5,10,50,100,500,1000]
    romantable = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    roman = ''

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        index = len(self.inttable) - 1
        self.composeRoman(index, num)

        return self.roman


    def composeRoman(self, index, num):

        if index < 0 or num == 0:
            return
        elif index > 0: 
            if index % 2 == 0:
                sindex = index - 2
            else:
                sindex = index - 1
        else:
            sindex = -1 
            

        base = self.inttable[index]
        q = num / base 
        r = num % base 

        print '----------'
        print 'num is %d,q is %d, r is %d, base is %d, sindex is %d' % (num, q, r, base, sindex)

        if sindex != -1 and base - num <= self.inttable[sindex] and base - num > 0:
            self.roman = self.roman + self.romantable[sindex] + self.romantable[index]
            r = num - (self.inttable[index] - self.inttable[sindex])
            index = sindex
            print 'roman is %s' % self.roman
            print 'r is %d' % r
        elif q > 3:
            self.roman = self.roman + self.romantable[index] + self.romantable[index+1]
            index = index - 1

            print '!!'
            if base - r <= self.inttable[sindex]:
                None
            else:
                index = index - 1
        else:
            for i in range(q):
                self.roman = self.roman + self.romantable[index] 

            if sindex != -1 and base - r <= self.inttable[sindex] and base - r > 0:
                None
            else:
                index = index - 1

        self.composeRoman(index, r)

# class Solution2(object):

if __name__ == '__main__':

    s = 19 
    print 'please input integer:'
    ans = raw_input()

    print Solution().intToRoman(int(ans))
