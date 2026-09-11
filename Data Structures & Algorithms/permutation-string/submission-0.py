class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26

        for c in s1:
            freq1[ord(c) - ord('a')] += 1

        freq2 = [0] * 26
        window_size = len(s1)

        for i in range(window_size):
            c = s2[i]
            freq2[ord(c) - ord('a')] += 1


        if freq1 == freq2:
            return True
        
        for i in range(window_size, len(s2)):
            freq2[ord(s2[i]) - ord('a')] += 1
            freq2[ord(s2[i - window_size]) - ord('a')] -= 1

            if freq1 == freq2:
                return True


        return False 
        