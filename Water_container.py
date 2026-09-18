class Solution:
    def maxArea(self, height: list[int]) -> int:
        big_container = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            
            current_area = width * current_height
            if current_area > big_container:
                big_container = current_area
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return big_container



solucao = Solution
print(f"Resultado funcao = {solucao.maxArea(solucao,height=[2,0])}")