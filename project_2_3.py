import scipy.stats as stats 
p = 0.04
x = 6
prob = stats.geom.pmf(x, p)
print(f"P(X={x}) : {prob:.3f}")
