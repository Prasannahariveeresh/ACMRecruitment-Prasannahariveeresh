sq_sum = lambda x: (x*(x+1)*((2*x) + 1))/6
sum_sqred = lambda x: ((x*(x+1))/2)**2

n = 100
diff = sum_sqred(n) - sq_sum(n)
print(diff)