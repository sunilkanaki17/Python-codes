class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sub=[]
        m=len(nums)
        for i in range(m):
            for j in range(i+1,m+1):
                sub.append(len(set(nums[i:j]))**2)
        return sum(sub)