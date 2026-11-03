s ="welcome in sgsits"
Vowel=0
Cons=0
for ch in s :
    if ch in "aeiou":
        Vowel+=1
    else:
        Cons+=1
print("vowel is",Vowel)
print("cons is",Cons)