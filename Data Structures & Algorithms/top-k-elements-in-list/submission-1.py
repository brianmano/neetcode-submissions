class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final = defaultdict(int)
        for i in nums:
            final[i] += 1  

        items = list(final.items())
        print(items)
        
        # # bubble sort
        # n = len(items)
        # for i in range(n):
        #     for j in range(0, n - i - 1): 
        #         if items[j][1] < items[j + 1][1]:  
        #             items[j], items[j + 1] = items[j + 1], items[j]

        # Use .sort() to sort items by frequency in descending order
        items.sort(key=lambda x: x[1], reverse=True)
        
        result = []

        for i in range(k):
            result.append(items[i][0])
        
        return result
