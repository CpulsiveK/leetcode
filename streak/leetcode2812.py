from collections import deque
from typing import Deque, List


class Solution:
    

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def in_bounds(r, c):
            return min(r, c) >= 0 and max(r, c) < N
        
        def multisourceBFS():
            queue = deque()
            min_dist = {}

            for r in range(N):
                for c in range(N):
                    if grid[r][c]:
                        queue.append([r, c, 0])
                        min_dist[(r, c)] = 0
            
            while queue:
                r, c, dist = queue.popleft()
                neighbours = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

                for nei_r, nei_c in neighbours:
                    if in_bounds(nei_r, nei_c) and (nei_r, nei_c) not in min_dist:
                        min_dist[(nei_r, nei_c)] = dist + 1
                        queue.append([nei_r, nei_c, dist + 1])
            
            return min_dist
        


                    


solution: Solution = Solution()
print(solution.maximumSafenessFactor([[1,0,0],[0,0,0],[0,0,1]]))