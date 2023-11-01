class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sub=[]
        sum=0
        m=len(nums)
        for i in range(m):
            for j in range(i+1,m+1):
                sub.append(nums[i:j])
        for i in range(len(sub)):
            sum+=len(set(sub[i]))**2
        return sum