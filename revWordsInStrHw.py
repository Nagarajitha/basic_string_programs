s = "this is python class"
new_s = ''
word = ''

for ch in s:
    if ch != ' ':
        word += ch
    else:
        new_s = word + ' ' + new_s
        word = ''

# Add the last word to the new_s
new_s = word + ' ' + new_s

print(new_s[:-1])  # Removing the trailing space
