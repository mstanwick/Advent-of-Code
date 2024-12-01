import re

# Create a list based on the puzzle data provided in a text file
with open('puzzle_input.txt') as f:
    lines = [line.rstrip() for line in f]

# In the puzzle data provided, two items are on each line. We need to split
# each item in each line into separate items.
lines_split = []
for item in lines:
    lines_split += re.split(' +', item)

# Split the two columns into two different lists.
list_1 = []
list_2 = []
x = 0

for item in lines_split:
    if x == 0 or x % 2 == 0:
        list_1.append(item)
    else:
        list_2.append(item)
    x += 1


# Sort the lists smallest to largest
list_1.sort()
list_2.sort()

total_distance = 0
y = 0

# Iterate through the lists, getting the difference between each item, then
# adding that difference to total_distance
for y in range(len(list_1)):
    list_1_item = int(list_1[y])
    list_2_item = int(list_2[y])

    # We don't want negative numbers, so find which item is larger to subtract
    # from then add that difference to total_distance.
    if list_1_item >= list_2_item:
        item_distance = list_1_item - list_2_item
    else:
        item_distance = list_2_item - list_1_item
    total_distance += item_distance

# Print the answer to the solution.
print(total_distance)

similarity = 0
similarity_count = 0

# Iterate through each list, checking how many times an item in the first list
# occurs in the second list. Keep track of the similarity count to multiply
# against the item. So if "1" from the first list is found 10 times in the
# second list, the similarity should be 1 * 10. Once you get the product, add
# that to the total_similarity.
for list_1_item in list_1:
    for list_2_item in list_2:
        if list_1_item == list_2_item:
            similarity_count += 1
            print(f"{list_1_item} == {list_2_item}. Similarity count = \
            {similarity_count}")
    similarity += int(list_1_item) * similarity_count
    print(f"{list_1_item} similarity {similarity_count}, \
    total_similarity = {similarity}")
    similarity_count = 0

# Print the answer to the solution.
print(similarity)
