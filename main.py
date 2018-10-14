import opentext
"""ans = input(
	"Do you want to looking for keyword on Google (y or yes to continue): ")"""
ans = "y"

if (ans == 'y' or ans == 'yes'):
	print("-> Connecting ... Done!\n-> Waiting for Google... Done!\n-> Ready")
	a = opentext.read_file("test")  # replace test with dir of key word file
	b = opentext.get_key_word("test")
	print("\nList of key word: " + str(b))
	opentext.search(a)
else:
	print("\n...Exiting application...\n")
