s="we love python we are python developers"
#we python
l = s.split()
new_s = ""
freq= 0

for word in l:
    if l.count(word) > freq:
        freq = l.count(word)
        new_s = word
    elif l.count(word) == freq and word not in new_s:
        new_s += " " + word

print( new_s)
