def get_sublist(lst, start_idx, end_idx):
    return lst[start_idx:end_idx:2]

input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

sublist = get_sublist(input_list, start_index, end_index)
print(sublist)
