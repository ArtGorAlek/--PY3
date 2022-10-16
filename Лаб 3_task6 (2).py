list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max = list_numbers[0]
ind_max = 0
for i, current_elem in enumerate(list_numbers):
    if current_elem > max:
        max = current_elem
        ind_max = i

list_numbers[-1], list_numbers[ind_max] = max, list_numbers[-1]
print(list_numbers)

