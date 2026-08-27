class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        long_length = 0
        char_set = set(s)

        for c in char_set:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                long_length = max(long_length, r - l + 1)

        return long_length






        


            
                

        




        return long_length
        
        

        