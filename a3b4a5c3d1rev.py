s = "aaabbbbaaaaacccd"
new_s = ""

count = 1  

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        new_s += str(count) + s[i-1]
        count = 1



print(new_s+str(count) + s[-1]
)
