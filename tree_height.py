#Sergejs Filatovs 221RDB111 16. grupa

import sys
import numpy
import threading

def compute_height(num_nodes, parents):
    parent=numpy.zeros(num_nodes)
    def height(i):
        if parent[i] !=0:
            return parent[i]
        if parents[i] == -1:
            parent[i] = 1
        else:
            parent[i]=height(parents[i]) +1
        return parent[i]
    
    for i in range(num_nodes):
        height(i)
    return int(max(parent))

def main():
    mode = input()
    if "F" in mode:
        filename = input()
        if "a" not in filename:
           with open(str("test/"+filename), mode = "r") as f:
               g = int(f.readline())
               parentOfNode = list(map(int, f.readline().split()))
        else:
            print("kļūda")
    elif "I" in mode:
        g = int(input())
        parentOfNode = list(map(int, input().split()))
    else: 
        print("kļūda")
    print(compute_height(g, parentOfNode))
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
