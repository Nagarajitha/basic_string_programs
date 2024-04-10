s = "engineering"
new_s = ""

freq = 0

for ch in s:
    if s.count(ch) > freq:
        freq = s.count(ch)
        new_s = ch
    elif s.count(ch) == freq and ch not in new_s:
        new_s += ch

print(new_s)
