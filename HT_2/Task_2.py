# Write a script which accepts two sequences of comma-separated colors from user. Then print out a set containing
# all the colours from color_list_1 which are not present in color_list_2.

sequence_1 = input("Input the first sequence of comma-separated colors: ")
sequence_2 = input("Input the second sequence of comma-separated colors: ")
color_list_1 = sequence_1.split(",")
color_list_2 = sequence_2.split(",")
print("Colours from color_list_1 which are not present in color_list_2:", set(color_list_1) - set(color_list_2))
