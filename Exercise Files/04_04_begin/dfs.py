"""
Python Data Structures - A Game-Based Approach
DFS maze solver.
Robin Andrews - https://compucademy.net/
The stack contains positions as (row, column) tuples. Predecessors are kept in a dictionary.
"""

from helpers import get_path, offsets, is_legal_pos, read_maze
from stack import Stack


def dfs(maze, start, goal):
    stack = Stack()
    stack.push(start)
    predecessors = {start: None}
    while not stack.is_empty():
        current = stack.pop()
        if current == goal:
            return get_path(predecessors, start, goal)
        for d in offsets:
            next_pos = (current[0] + offsets[d][0], current[1] + offsets[d][1])
            if is_legal_pos(maze, next_pos) and next_pos not in predecessors:
                stack.push(next_pos)
                predecessors[next_pos] = current
    return None


if __name__ == "__main__":

    # # Challenge
    # maze = [[0] * 4 for row in range(4)]
    # start_pos = (0, 0)
    # goal_pos = (3, 3)
    # result = dfs(maze, start_pos, goal_pos)
    # print(result)

    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    # Test 2
    maze = read_maze("mazes/mini_maze_dfs.txt")
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]

    # Test 3
    maze = read_maze("mazes/mini_maze_dfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = dfs(maze, start_pos, goal_pos)
    assert result is None
