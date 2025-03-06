# Step 1: Creating a dictionary to hold the student's data
student = {
    "name": "John Doe",
    "age": 20,
    "courses": ["Math", "History", "Physics"],
    "grades": {"Math": 90, "History": 85, "Physics": 88}
}

# Output: Displaying the initial student data
print("Initial Student Data:")
print(student)
print()

# Step 2: Accessing data from the dictionary
# Accessing individual values
name = student["name"]
age = student["age"]
courses = student["courses"]
grades = student["grades"]

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Courses: {courses}")
print(f"Grades: {grades}")
print()

# Step 3: Adding or updating data in the dictionary
# Adding a new course
student["courses"].append("Chemistry")

# Updating an existing grade
student["grades"]["Math"] = 95

# Output: Displaying updated data
print("Updated Student Data:")
print(student)
print()

# Step 4: Removing data from the dictionary
# Removing a course
student["courses"].remove("History")

# Removing a grade for Physics
del student["grades"]["Physics"]

# Output: Displaying data after removal
print("After Removal:")
print(student)
print()

# Step 5: Using the get() method to access a key safely
# Accessing the grade for 'Physics', which was removed earlier
physics_grade = student.get("grades", {}).get("Physics", "Grade not available")
print(f"Physics grade (using get()): {physics_grade}")
print()

# Step 6: Checking if a key exists in the dictionary
# Checking if the 'name' key exists
if "name" in student:
    print("The key 'name' exists in the dictionary.")
else:
    print("The key 'name' does not exist.")

# Checking if 'phone' key exists (a non-existent key)
if "phone" in student:
    print("The key 'phone' exists in the dictionary.")
else:
    print("The key 'phone' does not exist.")
print()

# Step 7: Merging another dictionary with the student dictionary
additional_info = {
    "address": "123 Main St, Springfield",
    "phone": "555-1234"
}

# Using update() to merge the dictionaries
student.update(additional_info)

# Output: Displaying merged data
print("After Merging Additional Info:")
print(student)
print()

# Step 8: Iterating over the dictionary
# Iterating over keys
print("Iterating over keys:")
for key in student:
    print(f"Key: {key}")

# Iterating over key-value pairs
print("\nIterating over key-value pairs:")
for key, value in student.items():
    print(f"{key}: {value}")
print()

# Step 9: Copying the dictionary
# Making a copy of the dictionary to avoid modifying the original
student_copy = student.copy()

# Modifying the copy (not affecting the original)
student_copy["name"] = "Jane Smith"

# Output: Displaying original and copied data
print("Original Student Data:")
print(student)

print("Modified Copy of Student Data:")
print(student_copy)
print()

# Step 10: Using dictionary comprehension
# Creating a new dictionary with course names and their respective grade percentages
course_percentages = {course: student["grades"].get(course, 0) / 100 * 100 for course in student["courses"]}

print("Course Percentages (Using Dictionary Comprehension):")
print(course_percentages)
print()

# Step 11: Nested Dictionaries (Example with more complex structure)
# Adding nested dictionaries to hold more detailed information about courses
student["course_details"] = {
    "Math": {"teacher": "Mr. Johnson", "credits": 3},
    "History": {"teacher": "Ms. Smith", "credits": 4},
    "Physics": {"teacher": "Dr. Brown", "credits": 3},
    "Chemistry": {"teacher": "Dr. White", "credits": 3}
}

# Output: Displaying student data with nested dictionaries
print("Student Data with Nested Course Details:")
print(student)
