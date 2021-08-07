sp1 = [True, False, True]

sp2 = [1, 15, 50, 100, 200]

if any (number > 50 for number in sp2):
	print ("Есть число больше 50")

if all (number > 0 for number in sp2):
	print ("Все числа больше нуля")


# если все элементы списка трушные
if all (sp1):
	print ("Все элементы трушные")
else:
	print('Не все элементы трушные')

if any (sp1):
	print ('Хотя бы 1 элемент - трушный')

if any (sp1) and not all(sp1):
	print("Есть элементы и трушные и фолсные")