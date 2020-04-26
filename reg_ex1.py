import re

msg="vivek is a python developer"

x=re.findall("[a-m]",msg)

x=set(x)

print(x)