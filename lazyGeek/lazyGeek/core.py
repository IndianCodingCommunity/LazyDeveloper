def greet(name):
    return f"Hello, {name}! Welcome to lazyGeek."


# Contributed by @piyushPb : github.com/piyushPb
def mean(*a):
    return sum(a)/len(a)

# Contributed by @piyushPb : github.com/piyushPb
def median(*a):
    sorted_a = sorted(a)
    n = len(sorted_a)

    if n % 2 == 1:
        return sorted_a[n // 2]
    else:
        mid1 = sorted_a[n // 2 - 1]
        mid2 = sorted_a[n // 2]
        return (mid1 + mid2) / 2


class LazyGeek:
    def __init__(self, value):
        self.value = value
