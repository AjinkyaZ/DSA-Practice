# Given string S, int N, return all combinations of letters of S
# upto size N, sorted lexicographically
from itertools import combinations

def main():
    S = raw_input("Enter String\n")
    n = int(raw_input("Enter max size of combinations\n"))
    S= sorted(S)
    scoms = []
    for i in range(1,n+1):
        each_size = list(combinations(S, i))
        for com in each_size:
            scoms.append(com)
    scoms  = [("").join(i) for i in scoms]
    for i in scoms : print i

if __name__ == "__main__":
    main()
