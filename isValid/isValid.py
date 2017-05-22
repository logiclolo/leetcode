class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        table = {
                '}':'{',
                ']':'[',
                ')':'('
                }

        stack = []

        for c in s:
            if table.has_key(c):
                if stack==[] or table[c] != stack.pop():
                    return False
            elif c in table.values():
                stack.append(c)

        return stack==[]



        """
        for c in s:
            if table.has_key(c):
                if len(stack) > 0 and table[c] == stack[-1]:
                    stack = stack[:-1]
                else:
                    return False
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        else:
            return False
        """

if __name__ == '__main__':

    print Solution().isValid('[]')
