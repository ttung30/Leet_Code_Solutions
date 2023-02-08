class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        pattern = list(pattern)
        merge = list(set(zip_longest(s,pattern)))
        if len(set(s))== len(merge) and len(set(pattern))==len(merge):
            return True
        return False
