class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        idea: use a stack
        """

        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            if s[i] == ')':
                if len(stack) > 0 and stack[-1] == '(': stack.pop()
                else: stack.append(s[i])
            if s[i] == '}':
                if len(stack) > 0 and stack[-1] == '{': stack.pop()
                else: stack.append(s[i])
            if s[i] == ']':
                if len(stack) > 0 and stack[-1] == '[': stack.pop()
                else: stack.append(s[i])
        
        return (len(stack) == 0)
        
