registry = set()

def register(active = True):
    def decorate(func):
        print(f"running register (active={active}->decorate({func}))")
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        
        return func
    return decorate

@register(active=False)
def f1():
    print("Running f1()")

@register()
def f1():
    print("Running f2()")
    