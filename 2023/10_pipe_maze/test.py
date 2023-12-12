def is_valid_move(matrix, visited, row, col):
    n = len(matrix)
    return 0 <= row < n and 0 <= col < n and matrix[row][col] == 0 and not visited[row][col]

def dfs(matrix, visited, row, col):
    visited[row][col] = True
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Up, Down, Right, Left

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if is_valid_move(matrix, visited, new_row, new_col):
            dfs(matrix, visited, new_row, new_col)

def find_enclosed_cells(matrix):
    n = len(matrix)
    loop_coordinates = []  # Store the coordinates of the loop
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                loop_coordinates.append((i, j))

    visited = [[False for _ in range(n)] for _ in range(n)]

    # Perform DFS from any point within the loop
    start_row, start_col = loop_coordinates[0]
    dfs(matrix, visited, start_row, start_col)

    # Identify enclosed cells
    enclosed_cells = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and matrix[i][j] == 0:
                enclosed_cells.append((i, j))

    return enclosed_cells

# Example usage:
matrix = [
    [0, 1, 2, 3, 0],
    [0, 10, 0, 4, 0],
    [0, 9, 0, 5, 0],
    [0, 8, 7, 6, 0],
    [0, 0, 0, 0, 0]
]

# enclosed = find_enclosed_cells(matrix)
# print("Enclosed cells:", enclosed)
