class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int

        idea:
        use a stack
        whenever an operand appears, pop stack[-1] & stack[-2] and push their result with the operand onto the stack
        """

        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                res = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
            elif tokens[i] == '-':
                res = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
            elif tokens[i] == '*':
                res = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
            elif tokens[i] == '/':
                res = int(float(stack[-2]) / stack[-1])
                stack.pop()
                stack.pop()
            else:
                res = int(tokens[i])
            stack.append(res)            

        return stack[0]
        
