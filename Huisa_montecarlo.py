from random import random

TRIES = 10000
hits = 0

for i in range(TRIES):
    r = random()
    x = -1 + 2 * r
    r = random()
    y = -1 + 2 * r

    if x * x + y * y <= 1:
        hits = hits + 1

# The ratio hits / tries is approximately the same as the ratio
# circle area / square area = pi / 4.

piEstimate = 4.0 * hits / TRIES
print("Estimated value of pi is", piEstimate)
