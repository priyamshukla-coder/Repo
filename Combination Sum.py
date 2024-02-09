class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(candidates , target , result , unique , idx):

            if target == 0:

                result.append(list(unique))

            while idx < len(candidates) and target >= candidates[idx]:

                unique.append(candidates[idx])

                backtrack(candidates , target - candidates[idx] , result , unique , idx)

                unique.pop()

                idx += 1

        result = []

        candidates.sort()

        backtrack(candidates , target , result , [] , 0)

        return result
        