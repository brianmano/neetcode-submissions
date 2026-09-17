class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:  
            return 0
        temp = sorted(set(nums))
        #print(temp)

        total = 1
        curr = 1
        
        for i in range(1, len(temp)):
            print(i)
            if temp[i] == 1 + temp[i-1]:  # Check for consecutive elements
                curr += 1
            else:
                total = max(total,curr)
                curr = 1
        total = max(total,curr)
        
        return total