class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        from collections import defaultdict

        emp_times = defaultdict(list)
        for name, time in access_times:
            emp_times[name].append(int(time[:2]) * 60 + int(time[2:]))
        result = []

        for name, times in emp_times.items():
            times.sort()
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] < 60:
                    result.append(name)
                    break
    
        return result