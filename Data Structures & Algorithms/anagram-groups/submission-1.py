class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            sortS = ''.join(sorted(s))
            result[sortS].append(s)
        return list(result.values())