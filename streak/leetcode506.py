from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        ranks: dict = {}
        answer: List = []

        for i in range(len(sorted_scores)):
            if i == 0:
                ranks[sorted_scores[i]] = "Gold Medal"
            elif i == 1:
                ranks[sorted_scores[i]] = "Silver Medal"
            elif i == 2:
                ranks[sorted_scores[i]] = "Bronze Medal"
            else:
                ranks[sorted_scores[i]] = str(i+1)
        
        for i in score:
            if i in ranks:
                answer.append(ranks[i])
                
        return answer

solution: Solution = Solution()
solution.findRelativeRanks([5,4,3,2,1])