class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #HashSet solution simple below:

        #seen = set()
        #for num in nums:
            #if num in seen:
                #seen.remove(num)
            #else:
                #seen.add(num)
        #return list(seen)[0]

        #Bit Manipulation Solution:

        res = 0
        for num in nums:
            res = num ^ res
        return res





        