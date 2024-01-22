class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int

        idea 2: stack O(n)
        use a stack that keeps tracks of (index, height); index will track the 1st index where the height can be used to calculate the area
         - while the new height is less than stack.top, pop stack.pop and calculate corresponding area (always a increasing stack)
         - push the new height onto stack
        after all heights are iterated, calculate corresponding area for each item in the stack
         - update max area if corresponding area is greater
        note that the corresponding area is calculated by minHeight * (Ind1 - Ind2)
        """

        max_area = 0
        stack = []
        for i in range(len(heights)):
            new_ind = i
            while len(stack) > 0 and heights[i] < stack[-1][1]:
                old_ind, old_height = stack.pop()
                max_area = max(max_area, old_height * (i - old_ind))  
                new_ind = old_ind
            stack.append((new_ind, heights[i]))
        
        for ind, height in stack:
            max_area = max(max_area, height * (len(heights) - ind))
        
        return max_area
        

