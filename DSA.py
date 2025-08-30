def fibo(n: int, list = []):
    if n <= 1:
        return n
    else:
        list.append(n)
        print(list)
        return fibo(n - 1) + fibo(n - 2)
    
# for i in range(int(input("Enter your input: "))): print(fibo(i))
print(fibo(4)) 

# ⚠️ Sum of natural numbers

def SumOfNaturalNum(n):
    if n == 1:
        return 1
    else:
        return n + SumOfNaturalNum(n - 1)

print(SumOfNaturalNum(5))

# ⚠️ Sum Of Series -> n + (n-2) + (n-4) + ....

def SumOfSeries(n) :
    if n == 0 or n == 1:
        return n
    else:
        return n + SumOfSeries(n - 2)

print(SumOfSeries(10))

# ⚠️ Exponential 

def power(n, m):
    if m == 0:
        return 1
    else:
        return n * power(n, m - 1)
    
print(power(2, 4))

# ⚠️ Greatest Common Divisor

def GCD(n1, n2 ):
    if n2 == 0:
        return n1
    return GCD(n2, n1 % n2)
print(GCD(20, 28))

# using loop 

n1, n2 = 20, 30
min_val = min(n1, n2)

for _ in range(min_val):
    if n2 == 0:
        print(n1)
        break
    n1, n2 = n2, (n1 % n2)
    min_val = min(n1, n2) 

# ⚠️ Reverse of string

def revStr(s):
    if len(s) == 0:
        return ''
    return revStr(s[1:]) + s[0]
    
print(revStr("Hello"))
