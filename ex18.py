# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one arg
def print_one(arg1):
	print(f"arg1: {arg1}")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shar")
print_one("First!")
