def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    return [list(column) for column in zip(*a)]
    # Your code here
    pass