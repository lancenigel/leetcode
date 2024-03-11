class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        subset = []

        def dfs(i):

            if i >= len(nums):
                res.append(subset.copy())
                return

            # include
            subset.append(nums[i])
            dfs(i + 1)

            # don't include
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


# .copy() is a shallow copy, this makes a 1 layer deep copy of an array which is suitable for single dimension arrays but not for
# multiple levels
# deep copy is for multiple dimension arrays
