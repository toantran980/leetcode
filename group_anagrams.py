class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            # Lists aren't hashable, so convert to a tuple
            groups[tuple(count)].append(s)

        return list(groups.values())