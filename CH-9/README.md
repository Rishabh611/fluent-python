# Decorater and Closures
- Callable that takes another function as an argument 
- A decorator may perform some processing with the decorated function, and returns it or replaces it with another function or callable object
```python
@decorate
def target():
    print("Running Target")
```
- will be same as 
```python
def target():
    print("Running target")
target = decorate(target)
```

- Three essential points that make a good summary of decoraters
    1. A decorater is a function or another callable.
    2. A decorater may replace the decorated function with different one.
    3. Decoraters are executed immediately when a module is loaded.

- A key feature of decoraters is that they run after the decorated function is defined. That is usually at import time 

# Closure
- A closure is a function with an extended scope that encompasses variables referenced in the body that are not global variables or local variables. Such variables must come from the local scope of an outer function that encompases the function.

# Variable Lookup Logic
When a function is defined, the Python bytecode compiler determines how to fetch a variable x that appears in it, based on these rules

    - If there is a global x declaration, x comes from and is assigned to the x global variable module.
    - If there is a nonlocal x declaration, x comes from and is assigned to the x local variable of the nearest surrounding function where x is defined.
    - If x is a parameter or is assigned a value in the function body, then x is the local variable.
    - If x is referenced but is not assigned and is not a parameter: —x will be looked up in the local scopes of the surrounding function bodies(nonlocal scopes).
    - If not found in surrounding scopes, it will be read from the module global scope.
    — If not found in the global scope, it will be read from __builtins__.__dict__.

# Decoraters in standard library
- three builtin functions designed to decorate method. `property` `classmethod` & `staticmethod`

# Memoization with `functools.cache`
- Memoization - an optimization technique that works by saving the results of previous invocations of an expensice function, avoiding repeat computations on previously used arguments
```python
import functools
from clockdeco0 import clock

@functools.cache
@clock
def fibonacci(n):
    if n<2:
        return n

    return fibonacci(n-2) + fibonacci(n-1)

```
# Single dispatch generic functions
- used for function overloading. The `@singledispatch` turns a function into a generic fucntion that can have different implementation depending on the functions first argument.

