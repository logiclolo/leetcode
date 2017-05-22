class Solution(object):
    def generateParenthesis1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        """
        This algorithm is defected!!
        """

        dynamic = ['(())', '()()']

        if n == 1:
            return ['()']
        elif n == 2:
            return dynamic

        for i in range(0,n-2):
            tmp = []
            for c in dynamic:
                tmp = tmp + ['('+c+')', c+'()', '()'+c]

            dynamic = tmp[:-1]
            
        return dynamic

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []

        self.dfs(0, n*2, n, '', [], res)

        return res

    def dfs(self, index, ceil, n, path, stack, res):
        if index == ceil:
            if stack == []:
                res.append(path)
        
        else:
            if n > 0:
                self.dfs(index+1, ceil, n-1, path+'(', stack+['('], res)

            if stack != [] and stack[-1] == '(' :
                self.dfs(index+1, ceil, n, path+')', stack[:-1], res)


if __name__ == '__main__':

    print Solution().generateParenthesis(4)
    print '----------'
    print ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
