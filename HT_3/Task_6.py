# Write a script to get the maximum and minimum VALUE
# in a dictionary.

dictionary = {1: 1, 22: 2, 333: 3, 4444: 4, 55555: 5}
min_key = min(dictionary, key = dictionary.get)
print('MIN: ', dictionary.get(min_key))
max_key = max(dictionary, key=dictionary.get)
print('MAX: ', dictionary.get(max_key))
