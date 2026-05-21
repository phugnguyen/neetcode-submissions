class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph as hash map
        # if cycle, return False
        # if no pre reqs, return True
        # once we complete a course, we set the pre req map to [] to show that we can complete it

        preMap = { i: [] for i in range(numCourses) }
        visited = set()

        for course, pre in prerequisites:
            preMap[course].append(pre)

        def canComplete(course):
            if course in visited:
                return False
            
            if preMap[course] == []:
                return True
            
            visited.add(course)
            for pre in preMap[course]:
                if not canComplete(pre):
                    return False

            visited.remove(course)
            preMap[course] = []

            return True



        for course in range(numCourses):
            if not canComplete(course):
                return False
        return True

        