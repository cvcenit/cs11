def transpose(matrix):
    if not matrix:
        return ()
    else:
        return matrix[0][0], matrix[1][0]