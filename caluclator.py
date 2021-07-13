# calculate the values that define the middle 95%
from scipy.stats import norm
# define distribution parameters
mu = 46
sigma = 25.8408
# create distribution
dist = norm(mu, sigma)
result = dist.cdf(91)
print((result))