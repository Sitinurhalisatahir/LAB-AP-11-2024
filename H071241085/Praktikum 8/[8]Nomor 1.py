import re

user = input('= ')

pattern = r'\A[a-zA-Z02468]{40}[13579\s]{5}\Z'

valid = re.match(pattern, user) != None

print('True' if len(user) == 45 and valid else 'False')