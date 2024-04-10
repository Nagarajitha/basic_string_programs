s='aaabbbbaaaaacccd'
#aaaaa


cs= s[0]
ms = s[0]

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        cs+= s[i]
    else:
        if len(cs) > len(ms):
            ms = cs
        cs= s[i]

# Check the last subsequence
if len(cs) > len(ms):
    ms = cs

print( ms)
