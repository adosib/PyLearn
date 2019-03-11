# Want: old_macdonald("macdonald") -> MacDonald
def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()

old_macdonald("macdonald")

# Master Yoda: return the words in the string in reverse order
def master_yoda(string):
    reversed_string = string.split()[::-1]
    return " ".join(reversed_string)

master_yoda("I am your father")

# Find 33: given a list of ints, return True if the array contains a 3 next to a 3 somewhere
def has_33(nums):
    for i in range(0, len(nums) - 1):  # Iterate through the list but stop before the last element
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

test1 = [1, 4, 5, 3, 1, 3]
test2 = [8, 9, 1, 3, 3, 2]
has_33(test1)
has_33(test2)

# Paper doll: given a string, return a string where for every character in the original there are three characters in the new
def paper_doll(string):
    result = ''
    for char in string:
        result += char*3
    return result

paper_doll("Hello")

# Summer of 69: Return the sum of the numbers in the array, except ignore sections of numbers starting
# with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# e.g. summer_69([2, 1, 6, 9, 11]) -> 14 ; summer_69([4, 5, 6, 7, 8, 9,]) -> 9
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
summer_69([4, 5, 6, 7, 8, 9,])
summer_69([2, 1, 6, 9, 11])
summer_69([4, 5, 6, 7, 8, 9, 12])

def summer_69_v2(arr):
    total = 0
    add = True
    for num in arr:
        if num != 6 and add:
            total += num
        elif num == 6 and add:
            add = False
        elif num != 9 and not add:
            continue
        else:
            add = True
            continue
    return total
summer_69_v2([4, 5, 6, 7, 8, 9])
summer_69_v2([2, 1, 6, 9, 11])
summer_69_v2([4, 5, 6, 7, 8, 9, 12])

# Spy Game: given a list of numbers, print True if the list contains 007 in order (not necessarily consecutively)
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if len(code) == 0:  # elif returns an index error exception
            break
    return len(code) == 0

spy_game([1, 2, 3, 0, 0, 7, 5])
spy_game([1, 0, 2, 4, 0, 5, 7])
spy_game([0, 0, 1, 5, 4, 9])

# Count primes: write a function that returns the number of prime numbers that exist up to and including a number
# 0 and 1 are not prime by convention
# The trick is to know that you can figure out whether a number is prime or not by testing all the prime numbers before it 
# as possible factors
def count_primes(num):
    if num < 2:
        return 0
    primes = [2]
    x = 3
    while x <= num:
        for y in primes:
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

count_primes(1000)