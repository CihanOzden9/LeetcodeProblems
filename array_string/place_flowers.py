

def func(flowerbed,n):
    # n çiçk sayıfı
    # flowerbed tarla listesi
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            bed_left = (i == 0 or flowerbed[i-1] == 0)
            bed_right = (i == len(flowerbed) - 1 or flowerbed[i+1] == 0)
            if bed_right and bed_left:
                flowerbed[i] = 1
                n -= 1
    return True if n <= 0 else False


arr = [0,0,1,0,1]
example = func(arr,1)
print(example)