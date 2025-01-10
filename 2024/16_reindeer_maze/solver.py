import re
import numpy as np

def read(file):
    with open(file, "r") as file:
        return file.read().split("\n")[:-1]  # Most typical case

def solver_alt2(input_file):
    lines = read(input_file)
    rows, cols = len(lines), len(lines[0])
    maze = np.zeros((rows, cols), dtype=str)
    for r in range(rows):
        for c in range(cols):
            maze[r, c] = lines[r][c]

    end = np.asarray(np.where(maze == "E"))
    start = np.asarray(np.where(maze == "S"))
    direction = np.array([0, 1])[:, None]  # east
    turn = lambda d: (d[:, 0] @ np.array([[0, -1], [1, 0]]))[:, None]
    look = lambda d: [d, turn(d), turn(turn(turn(d)))]


    best_paths = []
    best_scores = np.zeros((rows, cols)) + np.inf
    best_scores[*start] = 0

    queue = [(0, start, direction, [])]
    while len(queue):
        queue = sorted(queue, key=lambda x: x[0])
        score, pos, dir, path = queue.pop(0)
        path.append((tuple(pos[:, 0])))

        for check, ds in zip(look(dir), [1, 1001, 1001]):
            new_pos = check + pos
            if maze[*new_pos] != "#":
                new_score = score + ds
                if best_scores[*new_pos] >= new_score:
                    best_scores[*new_pos] = new_score
                    if (new_pos == end).all():
                        best_paths.append(path.copy())
                        score_at_end = new_score
                    queue.append((new_score, new_pos, check, path.copy()))
                elif best_scores[*new_pos] + 1000 == new_score:
                    queue.append((new_score, new_pos, check, path.copy()))

    visited = []
    for b in best_paths:
        visited += b
    return score_at_end, len(set(visited)) + 1

