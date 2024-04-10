s="this is python class"

l =s.split()
new_s=""
for ind in range(len(l)-1,-1,-1):
	new_s +=l[ind]+" "
print(new_s[:-1])