#Sergejs Filatovs 221RDB111 16. grupa

import sys


def read_input():
    n = int(input().strip())
    parents = list(map(int, input().split()))
    return n, parents

def compute_height(n, parents):
    height = [0] * n
    max_height = 0

    for vertex in range(n):
        if height[vertex] != 0:
            continue

        c_height = 0
        i = vertex
        while i != -1:
            if height[i] != 0:
                c_height += height[i]
                break
            c_height += 1
            i = parents[i]

        max_height = max(max_height, c_height)

        i = vertex
        while i != -1:
            if height[i] != 0:
                break
            height[i] = c_height
            c_height -= 1
            i = parents[i]

    return max_height

def main():
    n, parents = read_input()
    print(compute_height(n, parents))


    
    
if __name__ == '__main__':
    main()
