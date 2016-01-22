def naivesearch(s, p):
    n = len(s)
    m = len(p)
    index = "Not found"
    for i in range(n-m+1):
        if p == s[i:i+m]:
            index = i
    return index

def main():
    S = raw_input("Enter a string\n")
    A = raw_input("Enter search pattern\n")
    print naivesearch(S, A)


if __name__ == "__main__":
    main()
