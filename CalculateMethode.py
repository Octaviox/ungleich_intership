

low = int(input("Low	"))
up = int(input("Up	"))

def calculate(low,up):
	product = low
	while low in range(up):
		product = product * (low+1)
		low = low+1	
	print("Result	", product)




calculate(low,up)
