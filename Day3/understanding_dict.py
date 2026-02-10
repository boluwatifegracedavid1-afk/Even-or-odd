"""
studentsHome={
    "Tobi": "Alakuko",
    "Tolu": "Ait",
    "Tobi": "Ijoko"
}
print(studentsHome["Tobi"])

for student in studentsHome:
    print(student, studentsHome[student], sep=":")
"""

# multiple values in a dictionart using a list
students=[
    {"name": "Tobi", "house":"Alakuko", "age":"18"},
    {"name":"Tolu", "house":"Ait", "age":"14"},
    {"name":"Tomi", "house":"Ijoko", "age":"15"}
]
print(students[1])

for student in students:
    print(student["name"],student["house"], student["age"], sep= "/")