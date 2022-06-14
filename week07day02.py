# Exercise 1

print("Exercise 1")

def sum_to(n):
    total = 0
    for num in range(1,n+1):
        total += num
    return total

print(sum_to(10))
print("")

# Exercise 2

print("Exercise 2")

def largest(arr):
    return max(arr)

print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))
print("")

# Exercise 3

print("Exercise 3")

def occurrences(strng, char):
    return strng.count(char)

print(occurrences("fleep floop","ee"))
print("")

# Exercise 4

print("Exercise 4")

def product(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

print(product(-1, 4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))