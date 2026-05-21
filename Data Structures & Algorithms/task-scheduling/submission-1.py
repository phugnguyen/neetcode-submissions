class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each cycle is a unit of time 
        # use maxHeap to store task and occurences for efficient processes
        # use queue to hold tasks for their idle time, time at which they can be processesd is current time + n
        cnts = Counter(tasks)
        maxHeap = [-cnt for cnt in cnts.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt: #only append if there are items left
                    q.append([cnt, time + n]) # resulting count and next time that you can process
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time