import heapq
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # heap solution. time : O(nlogn) space : O(n)
        jobs = sorted(list(zip(startTime, endTime, profit)))
        heap = []
        currentProfit = 0
        maxProfit = 0
        for start, end, profit in jobs:
            while heap and heap[0][0] <= start:
                _, tempProfit = heapq.heappop(heap)
                currentProfit = max(currentProfit, tempProfit)

            heapq.heappush(heap, (end, currentProfit + profit))
            print(heap[0])
            maxProfit = max(maxProfit, currentProfit + profit)

        return maxProfit