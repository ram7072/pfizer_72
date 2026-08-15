Menu-driven program 
Scenario: Student Record System
Read N student names from the user.
Perform multiple operations like add, remove, insert, pop, search, count, index, slice, reverse, sort, join, and clear.
Print outputs after each operation so the user sees the changes.

Solution
# Step 1: Read number of students
n = int(input("Enter number of students: "))
students = []

# Step 2: Read student names
for i in range(n):
    name = input(f"Enter student {i+1} name: ")
    students.append(name)

print("\nInitial student list:", students)

# Step 3: Add new student
new_student = input("Enter a new student to add: ")
students.append(new_student)
print("After adding:", students)

# Step 4: Remove a student
remove_student = input("Enter a student to remove: ")
if remove_student in students:
    students.remove(remove_student)
print("After removing:", students)

# Step 5: Insert at position
insert_student = input("Enter a student to insert: ")
pos = int(input("Enter position (index): "))
students.insert(pos, insert_student)
print("After inserting:", students)

# Step 6: Pop last student
popped = students.pop()
print("Popped student:", popped)
print("After popping:", students)

# Step 7: Membership check
check_student = input("Enter a student to check: ")
print(f"Is {check_student} in list?", check_student in students)

# Step 8: Count occurrences
count_student = input("Enter a student to count: ")
print(f"{count_student} appears:", students.count(count_student), "times")

# Step 9: Find index
find_student = input("Enter a student to find index: ")
if find_student in students:
    print("Index of", find_student, ":", students.index(find_student))

# Step 10: Slice first 3
print("First 3 students:", students[:3])

# Step 11: Reverse list
students.reverse()
print("Reversed list:", students)

# Step 12: Sort alphabetically
students.sort()
print("Sorted list:", students)

# Step 13: Join into single string
joined = " | ".join(students)
print("Joined students:", joined)

# Step 14: Clear list
students.clear()
print("Final list after clearing:", students)
