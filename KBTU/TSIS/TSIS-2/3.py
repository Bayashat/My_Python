class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        size = len(nums)
        
        pairr = 0
        
        for i in range(size - 1):
            
            for j in range(i+1, size):
                
                if nums[i] == nums[j]:
                    pairr += 1
                    
        
        return pairr