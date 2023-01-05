class Solution:
    def findMinArrowShots(self, points):
        #sort the points with the second elem 
        points.sort(key=lambda x:x[1])
        arrowPosition = points[0][1]
        arrowCount = 1
        for i in range(1, len(points)):
            if arrowPosition >= points[i][0]:
                continue
            arrowPosition = points[i][1]
            arrowCount += 1
        return arrowCount

    def findMinArrowShotsSortWithFirstElem(self, points):
        #sort the points with the first elem, need to be in reversing order for the logic to work
        points.sort(key=lambda x:x[0], reverse=True)
        arrowPosition = points[0][0]
        arrowCount = 1
        for i in range(1, len(points)):
            if arrowPosition <= points[i][1]:
                continue
            arrowPosition = points[i][0]
            arrowCount += 1
        return arrowCount
