class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lista=[]
        lista_num = []
        for idx,x in enumerate(numbers):
            if lista_num.count(x) > 2:
                continue
            sub = target - x
            for i in lista:
                if sub + i[1] == target:
                    if idx < i[0]:
                        return [(idx+1),(i[0]+1)]
                    else:
                        return [(i[0]+1),(idx+1)]
            lista.append((idx,sub))
            lista_num.append(x)
            lista_num.append(x)

solucao = Solution
print(solucao.twoSum(solucao,numbers=[0,0,3,4],target=0))
