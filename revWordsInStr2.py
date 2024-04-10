s = "this is python class"

l=s.split()
for ind in range(len(l)):
    l[ind] = l[ind][::-1]
print(" ".join(l))