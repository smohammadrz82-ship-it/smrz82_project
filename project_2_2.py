import scipy.stats as stats 

# قسمت الف
x = 5
n = 5
p = 2 / 3
prob = stats.binom.pmf(x, n, p)
print(f"P(X={x}) : {prob}")
print(80 * '*')

# قسمت ب
sum_probs = 0
x_values = [3, 4, 5]
for x in x_values:
    prob = stats.binom.pmf(x, n, p)
    sum_probs += prob 
print(f"P(X>={x_values[0]}) : {sum_probs}")
print(80 * '*')

#قسمت ج 
x = 2
prob = stats.binom.pmf(x, n, p)
print(f"P(X={x}) : {prob}")
