class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
	if len(strs) is 0:
	    return ''

	string = strs[0]
	total = len(strs)
	begin = 0
	end = 0 
	maxsub = ''

	for i in range(len(string)):
	    sub = string[0:(end+1)] 

	    for j in range(total):
		if strs[j][0:i+1] == sub: 
		    if j == total - 1:
			maxsub = sub
		else:
		    return maxsub
		 
	    end = end + 1

	return maxsub

    
    def longestCommonSubstring(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
	total = len(strs)
	begin = 0
	end = 0 
	maxsub = ''
	
	if len(strs) is 0:
	    return ''
	elif len(strs) is 1:
	    return strs[0]

	string = strs[0]

	print 'base is %s' % string

	for i in range(len(string)):
	    sub = string[begin:(end+1)] 

	    for j in range(total):
		if j is 0:
		    continue

		print '-------%dth---%s-----' % (j+1, strs[j]) 
		print 'sub: %s' % sub
		if sub in strs[j]: 
		    print 'match!'
		    if len(sub) > len(maxsub) and j == total - 1:
			maxsub = sub
			continue
		else:
		    print 'not match'
		    begin = end + 1		
		    break
		 
	    end = end + 1

	return maxsub


if __name__ == '__main__':

    # string = ['abc', 'ab', 'abccsdfsdf']
    # string = ['ab', 'cd', 'fe']
    # string = ["c","acc","ccc"] 
    string = ["abab","aba","abc"]

    print Solution().longestCommonPrefix(string)

	    
