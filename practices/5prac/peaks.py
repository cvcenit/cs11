def peaks(heights):
    res = []
    for i in range(1, len(heights) - 1):
        if heights[i] > heights[i + 1] and heights[i] > heights[i - 1]:
            res += [i]
    return res

print(peaks((2, 5, 5, 1, 2, 1, 3, 1, 9, 10, 8, 3, 9)))
