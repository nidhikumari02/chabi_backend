def sort_list_of_dicts(lst, key):
    return sorted(lst, key=lambda x: x[key])

fruits = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sorted_by_fruit = sort_list_of_dicts(fruits, "fruit")
print(sorted_by_fruit)
# for fruit in sorted_by_fruit:
#     print(fruit)

print()  # Print an empty line for separation

sorted_by_color = sort_list_of_dicts(fruits, "color")
for fruit in sorted_by_color:
    print(fruit)
