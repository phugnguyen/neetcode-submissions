class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # graph as hashmap
        # results array to return if len(results) == numCourses else []
        # use visited and cycle set
        # in dfs(canComplete)
        # if visited return True
        # if in cycle return False
        # if not dfs children return False
        # add to visited, add to results
        # remove from cycle

        preMap = { i: [] for i in range(numCourses) }
        for course, pre in prerequisites:
            preMap[course].append(pre)
            
        results = []

        visited, cycle = set(), set()

        def canComplete(course):
            if course in visited:
                return True
            if course in cycle:
                return False
            
            cycle.add(course)
            for i in preMap[course]:
                if not canComplete(i):
                    return False

            cycle.remove(course)
            visited.add(course)
            results.append(course)

            return True
    
        for i in range(numCourses):
            canComplete(i)

        if len(results) == numCourses:
            return results
        else:
            return []