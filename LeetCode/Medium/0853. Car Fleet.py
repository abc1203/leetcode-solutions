class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int

        idea:
        use a stack to keep track of arrival time
        1. sort the positions s.t. we look at closest cars to target first
        2. if a car has slower arrival time than stack.top, push it onto stack
        3. else ignore it since it belongs to the carfleet at stack.top
        """

        stack = []
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        for (p, s) in cars:
            arrival_time = float(target - p) / s
            if len(stack) == 0 or arrival_time > stack[-1]:
                stack.append(arrival_time)
        
        return len(stack)
        
