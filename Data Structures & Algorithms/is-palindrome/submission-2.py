class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""

        for i in s:
            if i.isalnum():
                new += i.lower()
        print(new)

        l = 0
        r = len(new)-1

        #print(r)

        while (l < r):
            if (new[l] != new[r]):
                return False
            l = l+1
            r = r-1
        return True