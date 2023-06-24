import re

string = 'Lilian'

pattern = re.compile(r"[A-Za-z0-9%$#@]{8,}\d")

password = 'wetfdysufjs234$9'
a = pattern.search(string)
check = pattern.fullmatch(password)
print(check)


