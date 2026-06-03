class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals
        # then go through and form results
        sortedIntervals = sorted(intervals)
        results = [sortedIntervals[0]]
        for x, y in sortedIntervals:
            if x <= results[-1][1]:
                results[-1][1] = max(y, results[-1][1])
            else:
                results.append([x, y])

        return results