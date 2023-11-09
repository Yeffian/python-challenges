import string

letters = string.ascii_letters

def encrypt(text, key):
	substitution_dict = {}
	result = ''

	for i in range(len(letters)):
		substitution_dict[letters[i]] = letters[(i + key) % len(letters)]

	for char in text:
		if char in letters:
			temp = substitution_dict[char]
			result += temp
		else:
			temp = char
			result += temp

	return result	

	
def decrypt(text, key):
	substitution_dict = {}	
	result = ""

	for i in range(len(letters)):
		substitution_dict[letters[i]] = letters[(i - key) % (len(letters))]
		
	for char in text:
		if char in letters:
			temp = substitution_dict[char]
			result += temp
		else:
			temp = char
			result += temp
	
	return result