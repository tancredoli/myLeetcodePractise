from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        def backtrack(nums, curr):
            if len(curr) == len(nums):
                self.ans.append(curr[:])

            for num in nums:  # 1st :(n) 2st : (n-1) nth: 1   1* 2 * 3 * ... * n = n!
                if num not in curr:
                    curr.append(num)
                    backtrack(nums, curr)
                    curr.pop()

        backtrack(nums, [])
        return self.ans
        # permutation: length n -> n!

if __name__ == '__main__':
    s = Solution()
    assert s.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]