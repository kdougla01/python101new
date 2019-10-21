print ("Hello World!")

name = input("What is your name? ")

print (f"Hello {name}")

age = int(input("What is your age? "))

if age >= 18:
	print ("You are an adult")
elif age >= 13:
	print ("You are a teenager!")
else:
	print ("You are a child")