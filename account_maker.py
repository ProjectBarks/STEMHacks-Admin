import hashlib
import string
import random
import json


def salter(size=20, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

first, last = input("Name: ").split(" ")
grade = ["Freshman", "Sophomore", "Junior", "Senior"][(int(input("(Freshman 1 - 4 Senior) Grade: ")) - 1)]
username = input("Username: ")
password = input('Password: ')
salt = salter()
salted_pass = hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

for i in range(0, 100):
    print("")

print(json.dumps({username: {"pass": salted_pass, "first": first, "last": last, "salt": salt, "grade": grade}}, indent=4, sort_keys=True))