class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        temp = {} 

        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))

            if key in temp:
                temp[key].append(strs[i])
            else:
                temp[key] = [strs[i]]  # Initialize the key with a list if it's new

        return list(temp.values())
            
            
            