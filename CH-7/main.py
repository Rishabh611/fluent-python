def factorial(n):
    '''returns n!'''
    return 1 if n<2 else n * factorial(n-1)
fact = factorial
print(fact)
fact(5)
print(list(map(factorial, range(11))))

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))

def reverse(str):
    return str[::-1]

print(sorted(fruits, key=reverse))


# old map
print(list(map(factorial, range(6))))

# new list comprehension
print([factorial(i) for i in range(6)])

# old filter
print(list(map(factorial, filter(lambda n: n%2, range(6)))))

# new list comprehension
print([factorial(i) for i in range(6) if i%2])

# using lamda
print(sorted(fruits, key=lambda word:word[::-1]))