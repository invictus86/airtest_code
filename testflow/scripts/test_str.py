str1 = '{kernelargs}{'
# str2 = str1.replace('{', '{{}').replace('}', '{}}')
# print(str1.find("{"))
str2 = ""
for str in str1:
    if str == "{":
        str = "{{}"
    if str == "}":
        str = "{}}"
    str2 = str2 + str
print(str2)
# print(str2)
# 12cdef
