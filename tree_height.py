#Sergejs Filatovs 221RDB111 16. grupa

import sys

def read_input():
    n = int(input().strip())
    parents = list(map(int, input().strip().split()))
    return n, parents

def compute_height(n, parents):
    tree = {}
    root = None
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            if parent not in tree:
                tree[parent] = []
            tree[parent].append(i)

    height = 1
    q = [root]
    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.pop(0)
            if node in tree:
                q += tree[node]
        if q:
            height += 1

    return height

def main():
    try:
        n, parents = read_input()
    except EOFError:
        print("Input ended unexpectedly", file=sys.stderr)
        sys.exit(1)



  
    height = compute_height(n, parents)
    print(height)




if __name__ == "__main__":
    main()
