# Python learning exercises

# Functions
def echo(thing):
	return thing

def swap(thing1, thing2):
	return thing2, thing1
	
# Arithmetic Functions
def reverse(x):
	return -x


def plus(cat, dog):
	return cat+dog


def main_arithmetic():
	print "reverse(4): ", reverse(4)
	print "plus(1,1): ", plus(1,1)
	print "plus(0,4): ", plus(0,4)


def main():
	print "echo(baseball bat): ", echo("baseball bat")
	print "swap('fame', 'fortune'): ", swap("fame", "fortune")
	print "swap(6, 9): ", swap(6, 9)
	main_arithmetic()

main()
	