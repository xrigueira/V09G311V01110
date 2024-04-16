# Get the factorial of a number
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

# Define factorial withtot recursion (using a loop)
def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

# Get the number of combinations
def combinations(n, m):
    return factorial(n) / (factorial(m) * factorial(n-m))

if __name__ == "__main__":
    n = 5
    m = 3
    print("The number of combinations is: ", combinations(n, m))
