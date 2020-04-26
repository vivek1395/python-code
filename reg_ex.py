import re

msg="vivek is a python developer"

x= re.search("vishal",msg)  # output is None
print(x)

x=re.search("python",msg) #<re.Match object; span=(11, 17), match='python'>
print(x)

x= re.search("^vivek",msg)  ##<re.Match object; span=(0, 5), match='vivek'>
print(x)
x= re.search("^python",msg) # None >> "^" looks the search key in the begining.
print(x)

x= re.search("developer$",msg) #<re.Match object; span=(18, 27), match='developer'>
print(x)

x= re.search("python$",msg) # None , the sentence does not end with python.
print(x)

x=re.search("python|java",msg) # "|" it will search either python or Java available
print(x)

x=re.findall("python|java",msg) # "|" findall gives the output "python"
print(x)

x= re.findall("python$",msg) # []
print(x)


