#!/usr/bin/python3
"""return a list of lists of integers representing the Pascal’s triangle of n"""

def pascal_triangle(n):
    if (n <= 0):
        return []
    elif (n == 1):
        return [[1]]
    elif (n == 2):
        return [[1],[1, 1]]
    
    result = [[1],[1, 1]]
    for i in range(3, n + 1):
        row = [1]
        for j in range(0, i - 1):
            if (j < (i - 2)):
                one = result[i - 2][j] + result[i - 2][j + 1]
                row.append(one)
            else:
                row.append(result[i - 2][j])
        result.append(row)
    return result
