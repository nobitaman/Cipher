def encrypt(text,s):
	result=""
	for char in text:
#---------Encrypt uppercase characters in plain text
      
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)
#---------Encrypt lowercase characters in plain text
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)
	print(result) 
	return result




#----------Main Function
text = input("enter string: ")
s = int(input("enter shift number: "))

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(text,s))