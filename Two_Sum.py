class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sublist = []
        for idx,x in enumerate(nums):
            sub = target - x
            for i in sublist:
                if sub + i[1] == target:
                    return [i[0],idx]
            sublist.append((idx,sub))

solucao = Solution

print(solucao.twoSum(solucao,nums=[-3,4,3,90], target=0))

