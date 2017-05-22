class Solution(object):

    def __init__(self):
        self.lookup = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
                }

    def letterCombinations(self, digits):
	if '' == digits: return []
	kvmaps = {
	    '2': 'abc',
	    '3': 'def',
	    '4': 'ghi',
	    '5': 'jkl',
	    '6': 'mno',
	    '7': 'pqrs',
	    '8': 'tuv',
	    '9': 'wxyz'
	}
	ret=['']
	for c in digits:
	    tmp=[]
            print 'tmp is'
            print tmp
            print 'ret is'
            print ret
	    for y in ret:
		print '-------y:%s-----------' % y
		for x in kvmaps[c]:
		    print '-------x:%s-----------' % x 
                    print '%s' % (y+x)
		    tmp.append(y+x)
	    ret=tmp
    
	return ret 

    def letterCombinations_1(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if len(digits) is 0:
            return []

        res = []
        self.dfs(digits, 0, '', res)

        print res
        return res
        

    def dfs(self, digits, index, path, res):
        if index == len(digits): 
            print path
            res.append(path)
            return

        for c in self.lookup[digits[index]]:
            self.dfs(digits, index+1, path+c, res)
        

if __name__ == '__main__':

    nums = [3,3]
    target = 6 

    obj = Solution()
    print obj.letterCombinations('23')
