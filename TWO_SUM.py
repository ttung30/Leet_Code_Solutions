class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for y in range(i+1,len(nums)): 
                b=nums[i]+nums[y]
                if y!=i and b==target :
                    return [i,y]
