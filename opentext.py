
# BEGIN

import googlesearch


def read_file(path):
	file = open(path, "r")
	a = file.readlines()
	for i in range(len(a)):
		a[i] = "Climate Change " + a[i].rstrip('\n')
	return a


def get_key_word(path):
	file = open(path, "r")
	a = file.readlines()
	for i in range(len(a)):
		a[i] = a[i].rstrip('\n')
	return a


def search(a):
	for i in range(len(a)):
		query = a[i]
		print("\n\tLooking on Google for " + a[i] + ":\n")
		for url in googlesearch.search(query, tld="com", num=3, stop=2, pause=2):
			f = open("website.txt", "a")
			f.write(url + '\n')
			print(" >>> " + url)


# EOF
