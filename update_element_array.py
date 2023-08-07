def update_elements(arr, elements, positions):
for i, pos in enumerate(positions):
arr[pos-1] = elements[i]

inputarr = [0, 1, 2, 3, 4]
elements = [5, 6]
positions = [2, 4]
elementsupdate_elements(arr, elements, positions)
# Print the updated array
print(arr)
