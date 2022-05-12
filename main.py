import random
from collections import OrderedDict

# Write a program that generates simulated student info
# Requirements:
# 1. user input for names
# 2. no ID duplicates
# 3. email generation: 2 first names, account for space, make 2 char initials

# input: 3 lists
# output: student info (name, id, email)

names = []
ids = []
emails = []

# loop that prompts users for 5 names
for i in range(5):
    name = input("Enter your first and last name: ")
    names.append(name)
    ids.append(random.randint(111111, 999999))

    # removing duplicates in ids list
    no_duplicate_ids = []
    for id in ids:
        if id not in no_duplicate_ids:
            no_duplicate_ids.append(id)

    [first, last] = name.split(" ")
    email = first[0] + last + str(ids[i])[-3:] + "@example.com"
    emails.append(email)

# enhancement - student emails with 2 first name initials
for name in names:
    if len(name) == 3:
        [first, middle, last] = name.split(" ")
        email = first[0] + middle[0] + last + str(ids[i])[-3:] + "@example.com"
        emails.append(email)
    elif len(name) == 2:
        [first, last] = name.split(" ")
        email = first[0] + last + str(ids[i])[-3:] + "@example.com"
        emails.append(email)
print(emails)
