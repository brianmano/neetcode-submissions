class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = list(s)
        temp.sort()

        temp1 = list(t)
        temp1.sort()

        if (len(temp) != len(temp1)):
            return False
        
        for i in range(len(temp)):
            if temp[i] != temp1[i]:
                return False

        return True