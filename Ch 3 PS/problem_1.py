name = input("Enter your name: ")

print("Your name is:", name, "and the length of your name is:", len(name))  # prints the name and its length
print(f"Good morning {name}, have a nice day!")  # using f-string for formatted output

letter = '''Dear <name>, 
you are invited to the annual gathering of our community. We look forward to seeing you there!
<date>'''

print(letter.replace("<name>", "Sudhanshu").replace("<date>", "June 15, 2024"))  # replacing placeholders with actual values

name = "Harry is a good  boy and  "

print(name.find("  "))

name = "Harry is a good  boy and  "

print(name.replace("  ", " "))
print(name) # Strings are immutable which means that you cannot change them by running functions on them

letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"

print(letter)