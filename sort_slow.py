def bubble_sort(x):
    n = len(x)
    for i in range(n):
        for j in range(n-i-1):
            already_sorted = True
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
                already_sorted = False
        if already_sorted:
            break
    return x

xlist=[1,9,5,3,7,8,6,2,4,0]
print(sorted(xlist))
print(bubble_sort(xlist))
