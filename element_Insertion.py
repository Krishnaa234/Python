def insert_elements(arr, elements, positions):
    for i in range(len(positions) - 1, -1, -1):
        position = positions[i] - 1  # Convert 1-based position to 0-based index
        element = elements[i]
        arr.insert(position, element)
    return arr

# Sample inputs
arr = [0, 1, 2, 3, 4]
elements = [5, 6]
positions = [2, 4]

result = insert_elements(arr, elements, positions)
print(result)  # Output: [0, 5, 1, 2, 6, 3, 4]
