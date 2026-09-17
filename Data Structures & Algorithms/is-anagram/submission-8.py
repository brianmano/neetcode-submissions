class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ok = list(s)
        ok.sort()

        ok1 = list(t)
        ok1.sort()

        if len(ok) != len(ok1):
            return False

        for x in range(len(ok)):
            if ok[x] != ok1[x]:
                return False

        return True