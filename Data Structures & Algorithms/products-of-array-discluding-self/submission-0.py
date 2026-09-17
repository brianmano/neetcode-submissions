class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        for i in range(len(nums)):
            temp = nums.copy()
            print(i)
            temp.pop(i)
            print(temp)
            product = 1
            for num in temp:
                product *= num
            final.append(product)
        return final