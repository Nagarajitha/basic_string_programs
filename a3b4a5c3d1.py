s='a3b4a5c3d1'
new_s =""
for ind in range(0,len(s),2):
	new_s+=s[ind]*int(s[ind+1])
print(new_s)