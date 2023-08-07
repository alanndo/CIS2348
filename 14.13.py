# 2133915
# Alan Do

num_calls = 0

def partition(user_ids,low,high):
    i = (low-1)
    mid = (low+high)//2
    pivot = user_ids[mid]

    user_ids[mid], user_ids[high] = user_ids[high], user_ids[mid]

    for j in range(low,high):
        if user_ids[j] <= pivot:
            i = i +1
            user_ids[i], user_ids[j] = user_ids[j], user_ids[i]
    user_ids[i+1], user_ids[high] = user_ids[high], user_ids[i+1]
    return (i+1)


def quicksort(user_ids,low,high):
    global num_calls
    num_calls +=1
    if len(user_ids) == 1:
        return user_ids
    if low < high:
        x = partition(user_ids,low,high)
        quicksort(user_ids,low,x-1)
        quicksort(user_ids,x+1,high)

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids,0,len(user_ids)-1)
    print(num_calls)
    for user_id in user_ids:
        print(user_id)