name = "jacob"

nameshort = name[0:4]  # slicing the string to get the first 4 characters
print(nameshort)  # prints "jaco"

char = name[0]  # accessing the first character of the string
print(char)  # prints "j"

negativeslice = name[-4:-2]
print(negativeslice) # prints "ac" (characters at index -4 and -3)
print(name[1:3]) # prints "ac" (characters at index 1 and 2)

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])

print(name[1:5:2]) # slicing with step, prints every 2nd character from index 1 to 4
word = "hello world"
print(word[0:5:3]) # prints "hl" (characters at index 0 and 3)