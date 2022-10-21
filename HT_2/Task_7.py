# Write a script to concatenate all elements in a list
# into a string and print it. List must include both
# strings and integers and must be hardcoded.

def concatenate_list_elements(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_elements([15, 'Anna', 26, 'sun']))
