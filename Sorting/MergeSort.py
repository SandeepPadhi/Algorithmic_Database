def merge(arr, aux, lo, mid, hi):
    for i in range(lo, hi + 1):
        aux[i] = arr[i]

    i, j = lo, mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > hi:
            arr[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            arr[k] = aux[j]
            j += 1
        else:
            arr[k] = aux[i]
            i += 1

def sort(arr, aux, lo, hi):
    if lo >= hi:
        return
    mid = lo + (hi - lo) // 2
    sort(arr, aux, lo, mid)
    sort(arr, aux, mid + 1, hi)
    merge(arr, aux, lo, mid, hi)