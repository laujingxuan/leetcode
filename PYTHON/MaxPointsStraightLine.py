from cmath import inf
import math


class Solution:
    def maxPoints(self, points):
        if len(points) == 1:
            return 1
        maxNumberPoints = 0
        for i in range(len(points)):
            noGradientTracking = {}
            for j in range(len(points)):
                if i != j:
                    gradient = 0
                    if points[i][0] - points[j][0] == 0:
                        gradient = math.inf
                    else: 
                        gradient = (points[i][1] - points[j][1])/(points[i][0] - points[j][0])
                    if gradient in noGradientTracking:
                        noGradientTracking[gradient] = noGradientTracking[gradient] + 1
                    else:
                        noGradientTracking[gradient] = 2
                    maxNumberPoints = max(maxNumberPoints, noGradientTracking[gradient])
            print("points[i]: " + str(points[i]))
        return maxNumberPoints

if __name__ == "__main__":
    test = Solution()
    # print(test.maxPoints([[1,1],[2,2],[3,3]]))
    # print(test.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
    # print(test.maxPoints([[3,3],[1,4],[1,1],[2,1],[2,2]]))
    print(test.maxPoints([[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]))