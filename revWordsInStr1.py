s = "this is python class"
new_l =[]
for word in s.split():
    new_l.append(word[::-1])
print(" ".join(new_l))