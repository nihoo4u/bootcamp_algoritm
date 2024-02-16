def quick_sort(x):
    if len(x)<2:
        return x
    pivot=x[0]
    remn=x[1:]
    less=[z for z in remn if z<=pivot]
    more=[z for z in remn if z>pivot]
    return quick_sort(less) + [pivot] + quick_sort(more)


