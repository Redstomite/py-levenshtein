import numpy as np

def distc(word1, word2):
    xlength = len(word1)+1
    ylength = len(word2)+1
    grid = np.zeros((xlength, ylength))
    for x in range(xlength):
        grid[x, 0] = x
        for y in range(ylength):
            grid[0, y] = y

        for x in range(1, xlength):
            for y in range(1, ylength):
                if word2[x - 1] == word2[y - 1]:
                    grid[x, y] = min(
                        grid[x - 1, y] + 1,
                        grid[x - 1, y - 1],
                        grid[x, y - 1] + 1
                    )
                else:
                    grid[x, y] = min(
                        grid[x - 1, y] + 1,
                        grid[x - 1, y - 1] + 1,
                        grid[x, y - 1] + 1
                    )
        print(grid)
        return (grid[xlength - 1, ylength - 1])
