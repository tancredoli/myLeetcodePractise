class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def addNum(self, num: int) -> None:

        # binary search approach
        l, r = 0, len(self.list) - 1
        while l <= r:
            mid = (l + r) // 2
            if num > self.list[mid]:
                l = mid + 1
            else:
                r = mid - 1
        self.list.insert(l, num)

    def findMedian(self) -> float:

        return self.list[len(self.list) // 2] if len(self.list) % 2 == 1 else (self.list[len(self.list) // 2] +
                                                                               self.list[len(self.list) // 2 - 1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()