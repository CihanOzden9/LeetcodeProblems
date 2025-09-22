

def func(height):
    left = 0
    right = len(height)-1
    area = (right - left) * min(height[right], height[left])
    
    while left < right:
            
        new_area = (right - left) * min(height[right], height[left])
        if new_area >= area:
            area = new_area
            print(f"{left} X {right}; {area}")
            
        if height[left] > height[right]:
            right -= 1
            
        elif height[left] <= height[right]:
            left += 1
        
    return area

arr = [1,8,6,2,5,4,8,3,7]
arr2 = [1,1,3,5,2,7,9,3,4]
print(func(arr))