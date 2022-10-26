# todo bubble sort in ascending order
def bubble_sort(ascending_arr):
    ascending_arr_len = len(ascending_arr)
    for i in range(ascending_arr_len - 1):
        flag = 0
        for j in range(0, ascending_arr_len - i - 1):
            if ascending_arr[j] > ascending_arr[j + 1]:
                ascending_arr[j + 1], ascending_arr[j] = ascending_arr[j], ascending_arr[j + 1]
                flag = 1
                if flag == 0:
                    break
    return ascending_arr


# todo bubble sort in descending order
def descending_bubble_sort(descending_arr):
    descending_arr_len = len(descending_arr)
    for i in range(descending_arr_len - 1):
        flag = 0
        for j in range(0, descending_arr_len - i - 1):
            if descending_arr[j] < descending_arr[j + 1]:
                descending_arr[j + 1], descending_arr[j] = descending_arr[j], descending_arr[j + 1]
                flag = 1
                if flag == 0:
                    break
    return descending_arr


if __name__ == '__main__':
    arr_list = [5, 3, 4, 1, 2]
    print("List sorted with bubble sort in ascending order: ", bubble_sort(arr_list))
    print("List sorted with bubble sort in descending order: ", descending_bubble_sort(arr_list))
