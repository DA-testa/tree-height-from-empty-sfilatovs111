#Sergejs Filatovs 221RDB111 16. grupa

import sys
import threading
import numpy


def atrast_maksimalo_augstumu(skaits, vecaki):
    maksimalais_augstums = 0
    augstumi = [0] * skaits
    for mezgls in range(skaits):
        if augstumi[mezgls] != 0:
            continue
        augstums = 0
        i = mezgls
        
        while i != -1:
            if augstumi[i] != 0:
                augstums += augstumi[i]
                break
            augstums += 1
            i = vecaki[i]
        maksimalais_augstums = max(maksimalais_augstums, augstums)
        i = mezgls
        
        while i != -1:
            if augstumi[i] != 0:
                break
            augstumi[i] = augstums
            augstums -= 1
            i = vecaki[i]


    return maksimalais_augstums


def main():
    ievades_veids = input()
    skaits = int(input())
    vecaki = list(map(int, input().strip().split()))

    print(atrast_maksimalo_augstumu(skaits, vecaki))



    
    
    

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
main()
