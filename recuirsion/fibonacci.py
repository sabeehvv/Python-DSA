def fibonaccia(n):
    if n <= 1:
        return n
    else:
        return fibonaccia(n-1) + fibonaccia(n-2)
print(fibonaccia(9))