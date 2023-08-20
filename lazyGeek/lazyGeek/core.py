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
    
# Contributed by @piyushPb : github.com/piyushPb

def mode(*a):
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    mode = []
    max_freq = max(d.values())
    for key in d:
        if d[key] == max_freq:
            mode.append(key)
    return mode

# Contributed by @piyushPb : github.com/piyushPb

def quickSort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quickSort(left) + middle + quickSort(right)

# Contributed by @piyushPb : github.com/piyushPb

def bubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

# Contributed by @piyushPb : github.com/piyushPb

def insertionSort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# Contributed by @piyushPb : github.com/piyushPb

def selectionSort(a):
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

# Contributed by @piyushPb : github.com/piyushPb
def binarySearch(a, x):
    low = 0
    high = len(a) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if a[mid] < x:
            low = mid + 1
        elif a[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Contributed by @piyushPb : github.com/piyushPb
def linearSearch(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

# Contributed by @piyushPb : github.com/piyushPb

def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

class LazyGeek:
    def __init__(self, value):
        self.value = value
