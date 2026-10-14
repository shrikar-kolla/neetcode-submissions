class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ## Simple hash set solution i came up with:
        #dups = set()
        #for num in nums:
            #if num not in dups:
                #dups.add(num)
            #else:
                #return num

        #Most optimal solution:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

            
        