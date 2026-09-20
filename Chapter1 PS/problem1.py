'''
1. Write a program to print Twinkle twinkle little star poem in python.
2. Use REPL and print the table of 5 using it.
3. Install an external module and use it to perform an operation of your interest.
4. Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
5. Label the program written in problem 4 with comments
'''
# problem 1
# print("""Twinkle, twinkle, little star, how I wonder what you are.  Up above the world so high, 
# like a diamond in the sky.  Twinkle, twinkle, little star, how I wonder what you are. 

# When the blazing sun is set, and the grass with dew is wet.  Then you show your little 
# light, twinkle, twinkle all the night.  Twinkle, twinkle little star, how I wonder what you 
# are. 

# Then the traveler in the dark thanks you for your tiny spark.  How could he see where to 
# go if you did not twinkle so?  Twinkle, twinkle little star, how I wonder what you are. 

# As your bright and tiny spark lights the traveler in the dark, though I know not what you 
# are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are.     

# """)

# problem 3
# import pyttsx3
# pyttsx3.speak(" keso bhiayo aur aapko kesa lag raha hai")

# problem 4
import os 

content = os.listdir(".")

for item in content:
    print(item)


# problem 5