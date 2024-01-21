class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]

        idea:
        use backtracking; when we currently have i '(' and j ')', we can either:
            1. add '(' until i is incremented to n
            2. add ')' until j is incremented to i
        so the order of finding well-form parens will be:
        ((())) -> (()()) -> (())() -> ()(()) -> ()()()

        note that we can find all combinations of parentheses (not well-formed) by altering the condition to closed_count < n
        """

        stack = []
        ans = []

        def backtrack(open_count, close_count):
            if open_count == n and close_count == n:
                ans.append("".join(stack))
                return
            
            if open_count < n:
                stack.append('(')
                backtrack(open_count+1, close_count)
                stack.pop()
            if close_count < open_count:
                stack.append(')')
                backtrack(open_count, close_count+1)
                stack.pop()
        
        backtrack(0, 0)
        return ans    

        
        
