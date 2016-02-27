# create a function that is similar to one of the Java lessons
print("Hy i'am a Product Calculater,i can calculate any Product from 1 to 4000!!!!  Choose your Borders")

under_border = int(input("Low Border	"))

upper_border = int(input("Upper Border	"))

product = under_border

while under_border in range(upper_border):

	product = product * (under_border +1)

	under_border = under_border + 1

print("Result", product)
