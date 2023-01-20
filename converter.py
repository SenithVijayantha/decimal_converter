print("""
		Decimal_to_Binary      - 1
		Decimal_to_Octal       - 2
		Decimal_to_Hexadecimal - 3
		""")

no = input("Enter your no of choice: ")

def Decimal_to_Binary(): 

	Decimal_no = int(input("Enter a Decimal No:"))
	Binary_no = ("")
	while True:
		Digit = Decimal_no % 2 
		Decimal_no = Decimal_no // 2
		Binary_no = Binary_no + str(Digit)
		if Decimal_no == 0:
			break

	Binary_no = Binary_no [::-1]
	print(Binary_no)

#Decimal_to_Binary()

def Decimal_to_Octal():
	Decimal_no = int(input("Enter a Decimal No:"))
	Octal_no = ("")
	while True:
		Digit = Decimal_no % 8 
		Decimal_no = Decimal_no // 8
		Octal_no = Octal_no + str(Digit)
		if Decimal_no == 0:
			break

	Octal_no = Octal_no [::-1]
	print(Octal_no)

#Decimal_to_Octal()

def Decimal_to_Hexadecimal():
	Decimal_no = int(input("Enter a Decimal No:"))
	Hexadecimal_no = ("")
	while True:
		Digit = Decimal_no % 16
		Decimal_no = Decimal_no // 16
		Hexadecimal_no = Hexadecimal_no + str(Digit)
		if Decimal_no == 0:
			break

	Hexadecimal_no = Hexadecimal_no [::-1]
	print(Hexadecimal_no)

#Decimal_to_Hexadecimal()

if no == "1":
	Decimal_to_Binary()
elif no == "2":
	Decimal_to_Octal()
else:
	Decimal_to_Hexadecimal()
