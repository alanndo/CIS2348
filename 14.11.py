# 2133915
# Alan Do

def selection_sort_descend_trace(arr):
    n = len(arr)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        print(" ".join(map(str, arr)))


if __name__ == "__main__":

    input_list = input().split()
    int_list = [int(num) for num in input_list]

    selection_sort_descend_trace(int_list)