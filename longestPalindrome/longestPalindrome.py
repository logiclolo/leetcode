class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        longest = ''
        start1 = 0
        start2 = 0 

        if len(s) == 0:
            return None
        elif len(s) == 1:
            return s

        for i in range(len(s)):
            iteration = min(i + 1, len(s) - (i + 1))

            for j in range(iteration):
                j = j + 1

                if i-j > -1 and s[i-j] == s[i+j] and (start1 + 1) == j:
                    start1 = j 

                if s[i-(j-1)] == s[i+j] and (start2 + 1) == j:
                    start2 = j 

                if start1 != j and start2 !=j:
                    break

            if start1 > 0:
                print 'start1 = %d' % start1
                print '(1)s[..] = %s' % s[i-start1:i+start1+1] 
                print '(1)longest = %s' % longest
                longest = max(longest, s[i-start1:i+start1+1], key = len)
            
            if start2 > 0:
                print 'start2 = %d' % start2
                print '(2)s[..] = %s' % s[i-(start2-1):i+start2+1] 
                print '(2)longest = %s' % longest
                longest = max(longest, s[i-(start2-1):i+start2+1], key = len)

            start1 = 0
            start2 = 0 
            
        if longest == '':
            return s[0]
        else:
            return longest

if __name__ == '__main__':

    s = 'ccd'
    s = 'aaabaaaa'
    s = 'gdsooosg'
    s = 'sa'
    s = 'azwdzwmwcqzgcobeeiphemqbjtxzwkhiqpbrprocbppbxrnsxnwgikiaqutwpftbiinlnpyqstkiqzbggcsdzzjbrkfmhgtnbujzszxsycmvipjtktpebaafycngqasbbhxaeawwmkjcziybxowkaibqnndcjbsoehtamhspnidjylyisiaewmypfyiqtwlmejkpzlieolfdjnxntonnzfgcqlcfpoxcwqctalwrgwhvqvtrpwemxhirpgizjffqgntsmvzldpjfijdncexbwtxnmbnoykxshkqbounzrewkpqjxocvaufnhunsmsazgibxedtopnccriwcfzeomsrrangufkjfzipkmwfbmkarnyyrgdsooosgqlkzvorrrsaveuoxjeajvbdpgxlcrtqomliphnlehgrzgwujogxteyulphhuhwyoyvcxqatfkboahfqhjgujcaapoyqtsdqfwnijlkknuralezqmcryvkankszmzpgqutojoyzsnyfwsyeqqzrlhzbc'
    print Solution().longestPalindrome(s)
