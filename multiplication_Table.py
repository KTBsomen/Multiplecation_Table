import numpy as np
print('\t\t....THIS IS S MULTIPLICATION TABLE....\n')
while True:
	x=int(input("write the number to multiply : "))
	y=int(input("\n\nenter the leanth : "))
	print("\n\n")
	for i in range(1,y+1):
		print(x, "×", i, "=",x*i,"\n")
		