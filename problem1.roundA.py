import sys
import math


def map_collision(grid, array):
    d = {}
    for i in range(len(array)):
        d[chr(ord('A')+i)] = array[i]
    collisions = False
    encoded_words = set()
    for word in grid:
        s = ''.join([d[c] for c in word])
        if s in encoded_words:
            collisions = True
            break
        else:
            encoded_words.add(s)

    return "YES" if collisions else "NO"


if __name__ == '__main__':
    T = int(input().strip())
    results = []
    for i in range(T):
        array = input().strip().split()
        N = int(input().strip())
        grid = []
        for rows in range(N):
            k = input().strip()
            grid.append(k)
        result = map_collision(grid, array)
        results.append(result) 
    for i, result in enumerate(results):
        print("Case #{}: {}".format(i+1, result))
