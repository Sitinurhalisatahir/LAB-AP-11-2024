import re

string_pattern = r'[A-Za-z24680]{40}[13579\s]{5}$'

string = input('input string: ')
match = re.match(string_pattern, string)


if len(string) == 45 and match:
    print('True')
else:
    print('False')
