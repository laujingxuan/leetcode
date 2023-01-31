# You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

# However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

# Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

class Solution:
    def bestTeam(self, scores, ages):
        sortedList = sorted(zip(ages, scores))
        sortedScores = [score for _, score in sortedList]
        memo = [0 for i in range(len(sortedScores))]
        overallMax = 0
        for i in range(len(sortedScores)):
            memo[i] = sortedScores[i]
            for j in range(i):
                if sortedScores[i] >= sortedScores[j]:
                    memo[i] = max(memo[i], memo[j] + sortedScores[i])
            overallMax = max(overallMax, memo[i])
        return overallMax

if __name__ == "__main__":
    test = Solution()
    scores = [4,5,6,5]
    ages = [2,1,2,1]
    print(test.bestTeam(scores, ages))