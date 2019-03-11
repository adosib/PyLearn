# Find the cube root of a perfect cube using exhaustive enumeration
x = int(input('Enter an integer: '))
for ans in range(0, abs(x) + 1):  # ans is a temp variable which is assigned 0 through abs(user input), inclusive
    if ans**3 >= abs(x):
        break
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print("Cube root of", x, 'is', ans)

# Finger exercise: Let s be a string that contains a sequence of decimal numbers separated by commas, 
# e.g., s = '1.23,2.4,3.123'. Write a program that prints the sum of the numbers in s.
total = 0
s = '1.23, 2.4, 3.123'
for num in s.split(sep = ","):
    total += float(num)
print(total)   

# Exhaustive enumeration to find approximation to square root of a number x
x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print('numGuesses =', numGuesses)
if abs(ans**2 - x) >= epsilon:
    print("Failed on square root of", x)
else:
    print(ans, 'is close to square root of', x)

# Using bisection search to approximate square root
x = 25
epsilon = 0.01
numGuesses = 0
low = min(0, x)
high = max(1.0, x)
ans = (high + low)/2  # Start at the middle
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)

# Using Newton-Raphson to approximate a square root
# Find x s.t. x**2 - 24 is within epsilon of 0
epsilon = 0.01
k = 24.0
guess = k/2
numGuesses = 0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    numGuesses += 1
print('Square root of', k, 'is about', guess, '\nNumGuesses =', numGuesses)

