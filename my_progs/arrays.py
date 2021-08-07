arr_a = [34, 545, 56, 5, "Hi!", "World"]
for i in range (len(arr_a)):
	print (arr_a[i])

print(arr_a[3])

#посчитать длину массива
print("Длина массива: ", len(arr_a))
 
#увеличить длину массива, способ 1
arr_b = [77, 88, 99]
arr_a.extend(arr_b)
#снова вывести на экран
for i in range (len(arr_a)):
	print (arr_a[i])

#посчитать длину массива
print("Длина массива: ", len(arr_a))

#увеличить длину массива, способ 2
arr_c = arr_a + arr_b

#снова вывести на экран
for i in range (len(arr_c)):
	print (arr_c[i])

#посчитать длину массива
print("Длина массива: ", len(arr_c))
