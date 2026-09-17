class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)
        for i in strs:
            print(i)
            count = [0] * 26
            for c in i:
                count[ord(c) - ord("a")] += 1
            final[tuple(count)].append(i)
        return final.values()
# Basically, for every entry in the list, you add 1 to each letter that it has, and it should
# have the same key for every anagram 