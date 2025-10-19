def column_to_rows(matrix):
    if not matrix:
        return ()
    else:
        return matrix[0][0], *column_to_rows(matrix[1:])

def rest_columns(matrix):
    if len(matrix) == 1:
        return (matrix[0][1:],)
    else:
        return matrix[0][1:], *rest_columns(matrix[1:])

def transpose(matrix):
    if not matrix[0]:
        return ()
    else:
        return column_to_rows(matrix), *transpose(rest_columns(matrix))

print(transpose((
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (8, 7, 6),
))
)

print(transpose((
    (1,),
))
)