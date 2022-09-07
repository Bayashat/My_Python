class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max = 0
        h = 0
        for i in gain:
            h += i
            if h> max:
                max = h
        return max