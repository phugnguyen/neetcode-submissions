"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        sortedIntervals = sorted(intervals, key=lambda x: x.start)
        results = [sortedIntervals[0]]
        for idx, interval in enumerate(sortedIntervals):
            if idx == 0:
                continue
            if interval.start < results[-1].end:
                return False
            else:
                results.append(interval)
        return True
