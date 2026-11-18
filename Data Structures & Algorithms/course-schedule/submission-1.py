class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)

        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            state[node] = 1
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            state[node] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True



        