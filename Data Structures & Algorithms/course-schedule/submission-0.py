class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create graph with with a map
        premap = { i: [] for i in range(numCourses) }
        for course, prereq in prerequisites:
            premap[course].append(prereq)

        # visitSet = all courses along current DFS path
        visitSet = set()

        # base case if seen or if no preReqs
        # add to visitSet
        # dfs all prereqs, if it ever returns false, then return false
        # can shorten by setting the preMap to [] after visiting
        # remove from visitSet
        def canFinishCourse(course):
            if course in visitSet: return False # cycle
            if premap[course] == []: return True # no prereqs

            visitSet.add(course)
            for pre in premap[course]:
                if not canFinishCourse(pre): return False
            visitSet.remove(course)
            premap[course] = []
            return True
    
        # call function
        for course in range(numCourses):
            if not canFinishCourse(course): return False

        return True
