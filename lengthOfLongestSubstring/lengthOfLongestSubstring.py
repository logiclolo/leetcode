class Solution(object):
    # my version
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        check = {}
        index_dict = {}
        substring = '' 
        max_substring = '' 

        for c in s:
            if c in check:
                if len(substring) > len(max_substring):
                    max_substring = substring

                # construct the new substring i.e. (remove CCs)xxxx(add CC)
                # remove characters which are prior to target character from the hash table
                for cc in substring:
                    substring = substring[1:]
                    if cc == c:
                        substring = substring + c
                        break
                    check.pop(cc, None)
            else:
                check[c] = True 
                substring = substring + c


        if len(substring) > len(max_substring):
            max_substring = substring

        return len(max_substring)


	
    # leetcode version
    def lengthOfLongestSubstring1(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):

            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength



if __name__ == '__main__':
    
       print Solution().lengthOfLongestSubstring("asdfvcdfeabh") 

