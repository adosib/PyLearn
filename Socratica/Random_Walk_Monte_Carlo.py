import random

def random_walk(n):
    """Return coordinates after 'n' block random walk."""
    x, y = 0, 0
    for i in range(n):
        # With each step, the direction in x or y can change in 1 of 4 possible ways
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return x, y

# Test
for i in range(25):
    walk = random_walk(10)
    print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))

# Suppose we take a random walk from home and if we walk 4 blocks or fewer, we walk back home;
# else, we take a cab.
# Question: what's the longest random walk you can take so that on average you end up
# four blocks or fewer from home?

# Monte Carlo simulation
number_walks = 10000

for walk_length in range(1,35):
    no_transport = 0 # Number of random walks that end 4 blocks or fewer from home
    for i in range(number_walks):
        x, y = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    percent_no_transport = float(no_transport) / number_walks
    print("Walk size = ", walk_length, "/ % of no transport = ", 100*percent_no_transport)

