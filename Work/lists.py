#lists.py
# This script demonstrates basic list operations in Python. 
names = ["Alice", "Bob", "Charlie", "Diana"]
nums = [1, 2, 3, 4, 5]

#split string into list
line = 'GOOG,100,490.10'
row = line.split(',')
print(row)  # Output: ['GOOG', '100', '490.10']

names.append("Eve")
print(names)  # Output: ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

names.insert(2, "Frank")
print(names)  # Output: ['Alice', 'Bob', 'Frank', 'Charlie', 'Diana', 'Eve']

names.remove("Bob")
print(names)  # Output: ['Alice', 'Frank', 'Charlie', 'Diana', 'Eve'] 

names[1] = "Grace"
print(names)  # Output: ['Alice', 'Grace', 'Charlie', 'Diana', 'Eve']

for name in names:
    print("Hello " + name)

names.index("Charlie")  # Output: 2

sorted_names = sorted(names) # names remains unchanged

names.sort()
print("sorted names:", names)  # Output: ['Alice', 'Charlie', 'Diana', 'Eve', 'Grace']

nums = nums * 2
print("nums are not doubled, use numpy instead:", nums)  # Output:  [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]