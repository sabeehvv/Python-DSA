def investment(n):
    m = 7
    s = n % 7
    k = n // 7
    total = 0
    a = 1
    for i in range(k+1):
        if i > k-1 :
            m = s
        for j in range(a,m+a):
            print(j)
            total += j
        a += 1


    return total

output = investment(10)
print(output)