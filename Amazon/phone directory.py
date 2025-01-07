# URL: https://practice.geeksforgeeks.org/problems/phone-directory4628/1
# Time Complexity: O(n)
#Problem: Phone Directory


class Solution:
    def displayContacts(self, n, contact, s):
        # code here
        contact = sorted(set(contact))
        result = []
    
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            matches = [entry for entry in contact if entry.startswith(prefix)]
            result.append(matches if matches else ["0"])
    
        return result