def sum_mins(seq):
    result = []
    for sub in every_sub(seq):
        result += [min(sub)]
    return sum(result)

def every_sub(seq):
    result = []
    for i in range(len(seq)):
        for k in range(0, len(seq) + 1):
            if k > i:
                result += [[*seq[i:k]]]
    return result

print(sum_mins((3, 1, 4, 5, 9, 1, 2, 3, 4, 5, 1, 2, 3, 4)))
print(sum_mins((3, 1, 4, 1, 5)))