import random

student_data = [
    {
        "Name": "Mary Jane",
        "ID": 1000000,
        "Email": "mjane@adadevelopersacademy.org"
    },
    {
        "Name": "Jones Smith",
        "ID": 1000001,
        "Email": "jsmith@adadevelopersacademy.org"
    }
]

# student names in separate list
names = ["ROSIE MARTINEZ", "JOE LIU",
         "SALLY SUE", "BOB JOHNSON", "DELIA AGHO"]

for name in names:
    id = random.randint(111111, 999999)
    id_str = str(id)
    last_digits = id_str[-3:]

    [first, last] = name.split(" ")
    email = first+last+last_digits+"@adadev.org"

    student = {
        "Name": name,
        "ID": id,
        "Email": email,
    }

    student_data.append(student)

print(student_data)
