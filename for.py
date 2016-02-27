#For and if  in Python
import random

print("#################","Welcome the the Python Casion you have 3 Trys to Win the Jackpot")
y = int(random.random()*10)

for i in range(3):
	if i <2:
		print("Try",3-i)
	else:	
		print("Last Try")
	
	x = int(input("Choose a number (1-10)		"))
 
	
	if x > 10:
		print("Please choose a numeber in 1-10	")
	elif x < 1:
		print("Please only nubers in 1-10")
	elif x == y:
		for i in range(5):
			print("$$$$$$$$$$")
		print("Bing Bing Bing	"+"Wooow you win 1000000$")
		for i in range(5):
			print("$$$$$$$$$$")
		break
	else :
		print (x)
		print ("Try again")
