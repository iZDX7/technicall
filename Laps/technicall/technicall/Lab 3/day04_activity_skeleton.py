"""
Day 4 Activity: Parse nested dictionaries (student database).
Tasks:
1) Get Alice's AI301 grade
2) Calculate Bob's GPA (weighted by credits)
3) Find all students in CS101
4) Get average grade across all courses
5) Find student with highest GPA
"""

students = {
    "S001": {
        "name": "Alice Chen",
        "courses": {
            "CS101": {"grade": 92, "credits": 3},
            "MATH201": {"grade": 88, "credits": 4},
            "AI301": {"grade": 95, "credits": 3},
        },
        "advisor": "Dr. Smith",
    },
    "S002": {
        "name": "Bob Lee",
        "courses": {
            "CS101": {"grade": 85, "credits": 3},
            "MATH201": {"grade": 90, "credits": 4},
        },
        "advisor": "Dr. Patel",
    },
}

# Task 1
print(students["S001"]["courses"]["AI301"]["grade"])

# Task 2
bob_grade1 = 85 * 3
bob_grade2 = 90 * 4
bob_gpa = (bob_grade1 + bob_grade2) / 7
print(bob_gpa)

# Task 3
for sid in students:
    if "CS101" in students[sid]["courses"]:
        print(students[sid]["name"])

# Task 4
grades = [92, 88, 95, 85, 90]
print(sum(grades) / len(grades))

# Task 5
alice_gpa = (92*3 + 88*4 + 95*3) / 10
bob_gpa = (85*3 + 90*4) / 7
print("Alice" if alice_gpa > bob_gpa else "Bob")
