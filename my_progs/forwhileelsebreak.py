
 

print ('-----------')


for i in range (0, 6):
	print (i)

array_a = ["one", "two", "three", "some", "any"]
for i in array_a:
	print (i)

array_b = [-4, 34,  -2, 243, -54, 55, -99]
for i in array_b:
	if (i>0):
		print (i)

array_c = [3, 4, 6, -4, -3, 2, 58, -98, 77]
for i in array_c:
	if (i==58):
		print ("Нашли 58!")
		break
	print (i)
else:
	print ("Не нашли 58")