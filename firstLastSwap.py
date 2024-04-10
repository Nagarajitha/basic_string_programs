s = "dont fire the fire"
l = s.split()
new_s = ""

for word in l:
    fl = word[0]
    ll = word[-1]
    word = ll+word[1:-1]+fl
    new_s += word + " "

print(new_s[:-1])
