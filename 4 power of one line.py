def switch_key_value(dictionary):
    return {value: key for key, value in dictionary.items()}

original_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

switched_dict = switch_key_value(original_dict)
print("{")
for key, value in switched_dict.items():
    print(f'    "{key}": "{value}",')
print("}")

