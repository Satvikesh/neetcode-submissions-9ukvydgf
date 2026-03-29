class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for n in nums :
            if n in seen:
                return True
            seen[n] = True
        return False

    '''
 
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
    
        return False
hashset = set()
    for i in nums:
        if i in nums:
            return True
        hashset.add(i)
    return False
return len(nums) != len(set(nums))


'''
