#Problem: High Access Employee
#URL: https://leetcode.com/problems/high-access-employees/submissions/1528896546/


class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        employee_access = defaultdict(list)
        for name, time in access_times:
            hours, minutes = int(time[:2]), int(time[2:]) 
            total_minutes = hours * 60 + minutes
            employee_access[name].append(total_minutes)

        high_access_employees = []
        for employee, times in employee_access.items():
            times.sort() 
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] < 60: 
                    high_access_employees.append(employee)
                    break 

        return high_access_employees