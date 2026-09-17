class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()  

        for i in range(len(nums)):
            # Skip duplicate values for the fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            a = nums[i]
            l, r = i + 1, len(nums) - 1 
            
            while l < r:
                current_sum = a + nums[l] + nums[r]
                
                if current_sum == 0:
                    final.append([a, nums[l], nums[r]])
                    
                    # skip thru duplicates (beside)
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    
                    # move both cause there are no duplicates, so this is the only pair combo
                    # like if u have 4 and 1, you aint gunna find another 1 or 4, so move both
                    l += 1
                    r -= 1
                elif current_sum < 0:
                    l += 1
                else:
                    r -= 1
        
        return final