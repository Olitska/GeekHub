# Write a script to check whether a value from user
# input is contained in a group of values.

def is_group_member(group, value_to_check):
    return value_to_check in group
group = [1, 2, 'u', 'a', 4, True]
print(group, "--> 2 -->", is_group_member(group, 2))
print(group, "--> 5 -->", is_group_member(group, 5))
