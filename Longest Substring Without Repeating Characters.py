class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        big_seq = ""
        seq = ""
        if len(s) <= 1:
            return len(s)
        for x in s:
            print(x)
            if x  in seq:
                if len(big_seq) <= len(seq):
                    big_seq = seq
                    if big_seq[-1] != x:
                        seq = big_seq.split(f"{x}")[1] + x
                    else:
                        seq = "" + x
                elif seq[-1] != x:
                    seq = seq.split(f"{x}")[1] + x
                else:
                    seq = "" + x
            else:
                seq = seq + x
        if len(seq) >= len(big_seq):
            return len(seq)
        else:
            return len(big_seq)


solucao = Solution
print(solucao.lengthOfLongestSubstring(solucao,s="bdeaeafeadcaddacd"))