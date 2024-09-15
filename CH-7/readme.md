- Functions in python are First-class objects
- The __doc__ attribute is used to generate the help text of an object.
- A function that takes a function as an argument or returns a function as the result is a higher order function

# Modern replacements of `map`, `filter` and `reduce`
- Since introduction of list comprehension and generator expressions `map` and `filter` are not important
- `reduce` was demoted from a built- in to the `functools`
- in most usecases `sum` is better

# Anonymous Function
- `lambda`

# The nine flavors of callable objects
- the call operator `()` may be applied to other objects besides functions. 
- to determine whether an object is callable, we can use the `callable()` built-in function.
- Nine callable types
    - user-defined function
        - created with `def` or `lambda`
    - Built-in function
        - a function implemented in `C` like `len` or `time.strftime`
    - Built-in methods
        - Method implemented in `C` like `dict.get`
    - methods
        - functions defined in body of class
    - classes
        - when run class invokes it's `__new__` method to create an instance, then `__init__` to initialize & finally return an instance to the caller
    - class instances
        - if a class defines a `__call__` method then it's instances maybe invoked as a functions
    - Generator functions
        - functions or method which use `yield` keyword in the body
    - Native coroutine functions
        - functions or methods defined using `async def`
    - Asynchronous generator functions
        - functions or methods defined using `async def` that have `yield` in their body

# User defined Callable
- Python objects may also be made to behave like functions. Implementing a `__call__` method.

# Packages for functional programming
## the operator module
- The operator module provides function equivalents for dozens of operators so we don't need to code trivial functions like multiplication, division etc.
- Another group of one-trick lambdas that operator replaces are functions to pick items from sequences or read attributes from objects: `itemgetter` and `attrgetter` are factories that build custom function to do that.

## Freezing Arguments with `functools.- Given apartial`
- Given a callable, it produces a new callable with some of the arguments of the original callable bound to predetermined value