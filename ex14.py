from sys import argv
# read the WYSS section for how to run this
script, user_name, dog_name = argv
prompt = '? '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"How is {dog_name} ?")
print("I'd like to ask you a few questions.")
print(f"do you like me {user_name}??")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print ("What kind of conputer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.  Not sure where that is.
And you have a {computer} computer. Nice.
""")
