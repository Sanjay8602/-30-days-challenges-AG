#problem link: https://practice.geeksforgeeks.org/problems/nuts-and-bolts-problem0431/1
#title: Nuts and Bolts Problem

class Solution:
    def matchPairs(self, n, nuts, bolts):
		# code here
        order = {'!': 0, '#': 1, '$': 2, '%': 3, '&': 4, '*': 5, '?': 6, '@': 7, '^': 8}
        def custom_sort(arr):
            arr.sort(key=lambda x: order[x])
        custom_sort(nuts)
        custom_sort(bolts)