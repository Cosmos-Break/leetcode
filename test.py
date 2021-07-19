height = [2,3,3,4,1 ]
i, j, res = 0, len(height) - 1, 0
while i < j:
    if height[i] < height[j]:
        res = max(res, height[i] * (j - i))
        i += 1
    else:
        res = max(res, height[j] * (j - i))
        j -= 1
print(res)
