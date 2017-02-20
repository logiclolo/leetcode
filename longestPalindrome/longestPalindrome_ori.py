class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        longest = ''
        start = 0
        flag = 0

        if len(s) == 0:
            return None
        elif len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        for i in range(len(s)):
            iteration = min(i + 1, len(s) - (i + 1))

            print '-------iteration is %d-------' % iteration
            # for j in range(iteration):
                # print '(%d,%d)' % (i, j)
                # if len(s) > 2 and i-(j+1) > -1 and s[i-(j+1)] == s[i+(j+1)]:
                    # start = max(start, j + 1)
                    # flag = 1
                    # print i-j-1
                    # print s[i-j-1]
                    # print 'start is %d' % start
                    # print 'flag is %d' % flag 
                # elif s[i-j] == s[i+(j+1)]:
                    # # start = max(start, j + 1)
                    # start = max(start, j)
                    # flag = 2
                    # print 'start is %d' % start
                    # print 'flag is %d' % flag 
                # else:
                    # break

            # if flag is 1:
                # longest = max(longest, s[i-start:i+start+1], key = len)  
                # print i
                # print 'longest is %s' % longest 
            # elif flag is 2:
                # # longest = max(longest, s[i-start:i+start+2], key = len)  
                # longest = max(longest, s[i-start:i+start+2], key = len)  
                # print i
                # print 'longest is %s' % longest 

            for j in range(iteration):
                print '(%d,%d)' % (i, j)
                j = j + 1
                if len(s) > 2 and i-j > -1 and s[i-j] == s[i+j]:
                    start = max(start, j)
                    flag = 1
                    print 'start is %d' % start
                    print 'flag is %d' % flag 
                else:
                    break

            if flag is 1:
                longest = max(longest, s[i-start:i+start+1], key = len)  
                print '(1)longest is %s' % longest 

            start = 0
            flag = 0

            for j in range(iteration):
                print '(%d,%d)' % (i, j)
                j = j + 1
                if s[i-(j-1)] == s[i+j]:
                    print s[i-j+1]
                    start = max(start, (j - 1))
                    flag = 2
                    print 'start is %d' % start
                    print 'flag is %d' % flag 
                else:
                    break

            if flag is 2:
                longest = max(longest, s[i-start:i+start+2], key = len)  
                print '(2)longest is %s' % longest 

            start = 0
            flag = 0

        if longest == '':
            return s[0]
        else:
            return longest




    def isPalindrome(self, s):

        if len(s) is 0:
            return False

        mid = len(s) / 2
        total = len(s) - 1

        for i in range(mid):
            if s[i] == s[total-i]:
                continue
            else:
                return False

        return True




if __name__ == '__main__':

    # s = 'ccd'
    # s = 'aaabaaaa'
    # s = 'ss'
    s = 'azwdzwmwcqzgcobeeiphemqbjtxzwkhiqpbrprocbppbxrnsxnwgikiaqutwpftbiinlnpyqstkiqzbggcsdzzjbrkfmhgtnbujzszxsycmvipjtktpebaafycngqasbbhxaeawwmkjcziybxowkaibqnndcjbsoehtamhspnidjylyisiaewmypfyiqtwlmejkpzlieolfdjnxntonnzfgcqlcfpoxcwqctalwrgwhvqvtrpwemxhirpgizjffqgntsmvzldpjfijdncexbwtxnmbnoykxshkqbounzrewkpqjxocvaufnhunsmsazgibxedtopnccriwcfzeomsrrangufkjfzipkmwfbmkarnyyrgdsooosgqlkzvorrrsaveuoxjeajvbdpgxlcrtqomliphnlehgrzgwujogxteyulphhuhwyoyvcxqatfkboahfqhjgujcaapoyqtsdqfwnijlkknuralezqmcryvkankszmzpgqutojoyzsnyfwsyeqqzrlhzbc'

    # print Solution().isPalindrome(s)
    print Solution().longestPalindrome(s)
