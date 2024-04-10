
def ch_count(word):
    count = 0
    for ch in word:
        count += 1
    return count


s = "practice all programming questions properly to get a job"


hl= 0
new_S = ""

for word in s.split():  
    cl = ch_count(word)
    if cl > hl:
        hl = cl
        new_s = word

print(new_s)

