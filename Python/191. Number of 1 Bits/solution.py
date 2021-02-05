class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= (n-1)
            cnt+=1
        return cnt

if __name__ == '__main__':
    n = int('00000000000000000000000000001011', 2)
    s = Solution()
    assert s.hammingWeight(n) == 3