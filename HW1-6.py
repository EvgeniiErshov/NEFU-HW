L = [10, 4, 5, 6, 7, 8]
def get_largest_perimeter(L):
    maxPerimeter = 0
    n = len(L)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
           for k in range(j + 1, n):
                if (L[i] + L[j] > L[k]) and (L[i] + L[k] > L[j]) and (L[k] + L[j] > L[i]) and (L[i] + L[j] + L [k] > maxPerimeter):

                    maxPerimeter = L[i] + L[j] + L[k]

    print (maxPerimeter)
print (get_largest_perimeter(L))