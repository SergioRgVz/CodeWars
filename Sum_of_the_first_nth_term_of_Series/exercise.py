def series_sum(n):
    i = 1
    sum = 1.00
    while(i < n):
        sum = sum + 1/(1+3*(i))
        i+=1
    return sum