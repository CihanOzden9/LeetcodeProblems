def func(grid):
    len_grid = len(grid)

    rows = [row[:] for row in grid]

    cols = []
    for i in range(len_grid):
        col = []
        for k in range(len_grid):
            col.append(grid[k][i])
        cols.append(col)


    combined = rows + cols

    result = set(map(tuple, combined))
    if len(result) == 1:
        return len_grid * 2
    return len_grid * 2 - len(result)










def func2(grid):
    column_counts = Counter(zip(*grid))
    row_counts = Counter(map(tuple, grid))
    
    result = sum([column_counts[col] * row_counts[col] for col in column_counts])
    
    return result




















arr = [[13, 13], [13, 13]]
print(func(arr))
