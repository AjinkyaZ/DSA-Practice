# print mean, median and mode for N items

def get_mmm(d):
    n = len(d)
    d = sorted(d)
    if n==1:
        return (d[0], d[0], d[0])
    sum=0.0
    for i in range(n):
        sum += float(d[i])
    mean = sum/n
    if n%2==0:
        median = (d[(n/2)-1]+d[(n/2)])*0.5
    else:
        median = d[(n//2)]
    mean = float(mean)
    #print d
    median = float(median)
    x = [(i, d.count(i)) for i in d]
    x.sort(key=lambda x: x[1], reverse=True)
    #print x
    mode = x[0][0]
    return (mean, median, mode)

def main():
    d = raw_input().split(" ")
    d = [float(i) for i in d]
    mean, med, mode = get_mmm(d)
    print "Mean ", mean
    print "Median ", med
    print "Mode ", mode

if __name__=="__main__":
    main()