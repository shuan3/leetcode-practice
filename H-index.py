class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        mx = 0
        for i, el in enumerate(citations, start = 1):
            mx = max(mx, min(i, el))
        return mx