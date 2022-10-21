# Write a script to remove values duplicates from dictionary. Feel free to hardcode
# your dictionary.

dictionary = {'Anna': 27, 'Serhii': 6, 'Anastasiia': 5, 'Emiliia': 5, 'Yuliia': 27}
result = {}
for key, value in dictionary.items():
    if value not in result.values():
        result[key] = value
print(result)
