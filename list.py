# Step 1: Create a list of fruits in a grocery store
fruits = ['apple', 'banana', 'cherry', 'date']
print("Initial list of fruits:", fruits)

# Step 2: Access elements using indexing
first_fruit = fruits[0]  # Access the first element
last_fruit = fruits[-1]  # Access the last element
print("First fruit:", first_fruit)
print("Last fruit:", last_fruit)

# Step 3: Slice the list to get a portion of it
subset_fruits = fruits[1:3]  # Get fruits from index 1 to 2 (excluding index 3)
print("Subset of fruits (index 1 to 2):", subset_fruits)

# Step 4: Modify an element in the list
fruits[2] = 'kiwi'  # Replace 'cherry' with 'kiwi'
print("List after modification:", fruits)

# Step 5: Add new elements to the list
fruits.append('elderberry')  # Add 'elderberry' to the end of the list
fruits.insert(1, 'grape')  # Insert 'grape' at index 1
print("List after adding new fruits:", fruits)

# Step 6: Remove an element by value
fruits.remove('banana')  # Remove 'banana' from the list
print("List after removing 'banana':", fruits)

# Step 7: Remove an element by index
removed_fruit = fruits.pop(3)  # Remove the fruit at index 3 ('date')
print("List after popping index 3:", fruits)
print("Removed fruit:", removed_fruit)

# Step 8: Delete an element by index
del fruits[2]  # Delete the fruit at index 2 ('kiwi')
print("List after deleting index 2:", fruits)

# Step 9: Check if a fruit is in the list
is_kiwi_present = 'kiwi' in fruits  # Check if 'kiwi' is in the list
print("Is 'kiwi' present in the list?", is_kiwi_present)

# Step 10: Concatenate two lists
vegetables = ['carrot', 'broccoli', 'spinach']
combined_list = fruits + vegetables  # Combine the fruits and vegetables list
print("Combined list of fruits and vegetables:", combined_list)

# Step 11: Repeat elements in the list
repeated_fruits = fruits * 2  # Repeat the list of fruits twice
print("List after repeating fruits:", repeated_fruits)

# Step 12: Sort the list of fruits
fruits.sort()  # Sort the fruits list in alphabetical order
print("Sorted fruits list:", fruits)

# Step 13: Reverse the list of fruits
fruits.reverse()  # Reverse the order of the fruits list
print("Reversed fruits list:", fruits)

# Step 14: List comprehension to create a new list with fruit lengths
fruit_lengths = [len(fruit) for fruit in fruits]  # Get the length of each fruit name
print("Lengths of each fruit name:", fruit_lengths)

# Step 15: Create a copy of the fruits list
fruits_copy = fruits.copy()  # Create a shallow copy of the list
print("Copied list of fruits:", fruits_copy)

# Step 16: Flatten a nested list (example with multiple lists inside)
nested_fruits = [['apple', 'banana'], ['kiwi', 'cherry'], ['date', 'elderberry']]
flattened_fruits = [fruit for sublist in nested_fruits for fruit in sublist]  # Flatten the nested list
print("Flattened list of fruits:", flattened_fruits)

# Step 17: Calculate the length of the final list
final_length = len(fruits)  # Find the length of the current fruits list
print("Final length of the fruits list:", final_length)
