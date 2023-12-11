from itertools import combinations

while 1:
    N = input().split()
    if N[0] == "0":
        break

    S = N[1:]

    for c in combinations(S, 6):
        print(" ".join(c))
        
    print()