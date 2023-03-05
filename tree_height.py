#Sergejs Filatovs 221RDB111 16. grupa


import sys
import threading
def calc_tree_height(num_nodes, ancestors):
    descendants = [[] for i in range(num_nodes)]
    
    root = None
    for i in range(num_nodes):
        if ancestors[i] == -1:
            root = i
        else:
            descendants[ancestors[i]].append(i)

            
            
    def dfs(node):
        if not descendants[node]:
            return 1
        return max([dfs(child) for child in descendants[node]]) + 1

    return dfs(root)



def main():
    num_nodes = int(input().strip())
    ancestors = list(map(int, input().split()))
    print(calc_tree_height(num_nodes, ancestors))

    
if __name__ == '__main__':
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    thread = threading.Thread(target=main)
    thread.start()

