s = "this is python class"
new_s = ''
for word in s.split():
    new_s += word[::-1]+" "
print(new_s[:-1])
print(new_s.strip(""))