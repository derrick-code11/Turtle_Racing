def binary_search(num_list, num):
    start = 0
    end = len(num_list) - 1
    num_found = False
    while start <= end and not num_found:
        middle = (start + end) // 2
        if num_list[middle] == num:
            num_found = True
        elif num_list[middle] < num:
            start = middle + 1
        else:
            end = middle - 1
    return num_found


print(binary_search([i for i in range(1000000)], 67))