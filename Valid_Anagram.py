class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for x in s:
                if x in t:
                    for idx,y in enumerate(t):
                        if x == y:
                            t = t[:idx] + t[idx+1:]
                            break
                else:
                    return False
            return True
        return False

solucao = Solution
print(solucao.isAnagram(solucao,s="anagram",t="nagaram"))