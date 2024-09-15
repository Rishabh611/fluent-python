registry = []

def register(func):
    print(f"running register({func})")
    registry.append(func)
    return func

@register
def f1():
    print("Running f1")

@register
def f2():
    print("Running f2")

def main():
    print("Running Main")
    print("Registry ->", registry)
    f1()
    f2()

if __name__ == "__main__":
    main()