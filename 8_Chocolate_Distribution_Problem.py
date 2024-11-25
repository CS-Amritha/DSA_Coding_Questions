
class Solution:

    def findMinDiff(self, arr,M):

        arr.sort()
        ans = float('inf')
        n = len(arr)

        for i in range(n-M+1):
            minWindow = arr[i]
            maxWindow = arr[i+M-1]
            
            diff = maxWindow - minWindow
            
            if ans > diff:
                ans = diff
        return ans
