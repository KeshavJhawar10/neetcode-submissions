class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_order = []
        prereq_map = {i: [] for i in range(numCourses)}

        for crs, prereq in prerequisites:
            prereq_map[crs].append(prereq)

        visiting = set()
        visited = set()

        def dfs(crs):
            if crs in visiting:
                return False

            if crs in visited:
                return True

            visiting.add(crs)

            for prereq in prereq_map[crs]:
                if not dfs(prereq):
                    return False

            visiting.remove(crs)
            visited.add(crs)
            course_order.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return course_order
        