factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

number = int(input("Enter a number: "))
result = factorial(number)
print(result)



