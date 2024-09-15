def deco(func):
    def inner():
        print("running inner()")
    return inner

@deco
def target():
    print("Running target()")

target()