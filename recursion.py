################################################
# Recursion Programming Exercise: log

def log(b, n):
    if n <= b:
        return 1
    else:
        return log(b, n/b)+1


print(log(2, 6))
print(log(10, 100))

################################################

# Recursion Programming Exercise: Multiply

def multiply(x, y):
    if x == 1:
        return y

    else:
        return multiply(x-1, y) + y


print(multiply(5, 4))
print(multiply(10, 10))

################################################

# Recursion Programming Exercise: Cumulative Sum

def sumtok(k):
    if k <= 0:
        return 0
    else:
        return sumtok(k - 1) + k


print(sumtok(5))
print(sumtok(3))

################################################

# Recursion Programming Exercise: Add odd values

def addOdd(n):
    if n <= 0:
        return 0

    if n % 2 != 0:
        return addOdd(n - 1) + n
    else:
        return addOdd(n-1)


print(addOdd(7))
print(addOdd(12))

################################################

# Recursion Programming Exercise: Count Characters

def countChr(str):
    if len(str) == 0:
        return 0

    count = 0
    if str[0] == "A":
        count = 1
    return count + countChr(str[1:])


print(countChr("ctcowcAt"))
print(countChr("AaweoijAAaropijA"))

################################################
