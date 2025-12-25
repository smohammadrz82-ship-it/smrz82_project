import scipy.stats as stats 
n = 10
p = 0.5
x_values = [7, 8, 9, 10]
sum_probs = 0
for x in x_values:
    prob = stats.binom.pmf(x, n, p)
    sum_probs += prob 

print(f"P(X>={x_values[0]}) : {sum_probs}")
