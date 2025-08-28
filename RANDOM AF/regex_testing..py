import re

email = input("Enter anything that includes an email at least: ")

pattern = "[\w\.-]+@[\w\.-]+\.\w+"

valid = re.findall(pattern, email)

print(valid)