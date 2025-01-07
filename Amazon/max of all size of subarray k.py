#Problem: find the maximum of all subarrays of size k
#Link: https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1


class Solution:
    #Function to find maximum of each subarray of size k.
    def maxOfSubarrays(self, arr, k):
        # code here
        if not arr or k == 0:
            return []
        n = len(arr)
        dq = deque()
        result = []
        for i in range(n):
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(arr[dq[0]])
        return result