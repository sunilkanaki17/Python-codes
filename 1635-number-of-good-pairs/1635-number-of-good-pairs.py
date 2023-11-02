class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    ans.append([i,j])
        return len(ans)
        