from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        freq_count = Counter(nums)
        freq_buckets = [[] for i in range(len(nums) + 1)]

        # Step 2: Place each number into its frequency bucket
        for n,c in freq_count.items():
            freq_buckets[c].append(n)

        # Step 3: Collect top k elements starting from highest frequency, append that to result
        result = []
        for i in range(len(freq_buckets) -1 ,0,-1):
            for n in freq_buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result
