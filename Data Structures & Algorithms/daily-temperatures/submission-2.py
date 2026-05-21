class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use stack to keep track of temps that are less than current item in stack
        # also keep track of index to update results array
        result = [0] * len(temperatures)
        stack = []
        # [0, 30]
        # empty

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                current = stack.pop()
                result[current[0]] = idx - current[0]
            stack.append([idx, temp])

        return result
