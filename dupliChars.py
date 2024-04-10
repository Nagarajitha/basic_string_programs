s="engineering"
new_s=""

for ch in s:
	if s.count(ch)>1 and (ch not in new_s):
		new_s+=ch
print(new_s)