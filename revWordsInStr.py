s = "this is python class"

rev_s = ''
word = ''

for ch in s:
    if ch != ' ':
        word = ch + word
    else:
        rev_s += word + ' '
        word = ''

if word:
    rev_s += word

print(rev_s)


