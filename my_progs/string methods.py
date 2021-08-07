str1 = 'Привет, мир!!! Как дела, народ'

# сделать маленькими
print(str1.lower())
# сделать большими
print(str1.upper())

# подсчет количества символов
print(str1.count('!'))

# проверяет, строковая ли это переменная
print(str1.isalpha())

str2 = 'sdfsdf'
# проверяет, числовая ли это переменная
print(str2.isdigit())

str3 = '5555'
print(str3.isdigit())



# вывести длину строки. Здесь не метод, а функция
print(len(str1))



print(str1.replace("мир", "друг"))
# заменяем пробелы на пустоту
print(str1.replace(" ", ""))

# разбить строку на список
str1_array = str1.split(' ')
print(str1_array)

# на практике
str2 = '01.jpg;02.jpg;34.jpg;sdf.jpg;sdf.jpg;dfd.jpg'
str2_array = str2.split(';')
print(str2_array)

# массив сохранить в одну строку, разделитель между ними - решетки 
imgs_array = ['01.jpg', '02.jpg', '34.jpg', 'sdf.jpg', 'sdf.jpg', 'dfd.jpg']
imgs_str = ';'.join(imgs_array)
print(imgs_str)


# Найти положение слова и вывести это на экран
print (str1.find('мир'))
print(str1.rfind('и'))
print(str1.rfind('и!!'))

# найти индекс и вывести на экран
print (str1.index('мир'))
print (str1.rindex('и'))
print (str1.index('и!!'))



