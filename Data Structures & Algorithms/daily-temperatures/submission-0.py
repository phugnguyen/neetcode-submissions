class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use monotonic decreasing stack, where you only append to the stack if the current value is less than
        # save index in stack so we know how to update the output
        result = [0] * len(temperatures)
        # stack = List[idx, temp]
        stack = [] 


        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                current = stack.pop()
                result[current[0]] = idx - current[0]
            stack.append([idx, temp])
        return result
