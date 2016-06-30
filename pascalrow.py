# given integer N, return (N+1)th row of pascal triangle
def get_pascalrow(N):
    N = N + 1
    res= []
    if N == 0:
        return res
    res= [[1]]
    for i in range(2,N+1):
        res.append([0]*i)
        res[i-1][0] = 1
        res[i-1][-1] = 1
        for j in range(1,i-1):
            res[i-1][j] = res[i-2][j-1]+res[i-2][j]
    return res[-1]

def main():
    n = int(raw_input("enter N for (N+1)th row of pascal triangle :\n"))
    result = get_pascalrow(n)
    print result

if __name__ == "__main__":
    main()