from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        prerequires_count = [0] * numCourses
        ncourses = defaultdict(set)
        topological_sort = []
        for a, b in prerequisites:
            prerequires_count[a] += 1
            ncourses[b].add(a)
        queue = deque([i for i, e in enumerate(prerequires_count) if e == 0])
        while queue:
            target = queue.popleft()
            ntargets = ncourses[target]
            topological_sort.append(target)
            for ntarget in ntargets:
                count = prerequires_count[ntarget]
                if count > 1:
                    prerequires_count[ntarget] -= 1
                elif count == 1:
                    prerequires_count[ntarget] -= 1
                    queue.append(ntarget)
        if len(topological_sort) == numCourses:
            return True
        else:
            return False


numCourses = 7
prerequisites = [[1, 0], [0, 3], [0, 2], [
    3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]
print(Solution().canFinish(numCourses, prerequisites))
