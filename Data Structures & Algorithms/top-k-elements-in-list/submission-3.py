class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        for i in range(len(nums)):
            if (nums[i] in temp):
                temp[nums[i]] += 1
            else:
                temp[nums[i]] = 1
        
        final = list(temp.items())
        #print(final)
        final.sort(key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(final[i][0])


        return result
        