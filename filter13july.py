my_str=input("Enter your name")
def vowel(n):
	my_vowel=['a','e','i','o','u','A','E','I','O','U']
	if n not in my_vowel:
	    return True
	        
print(list(filter(vowel,my_str)))