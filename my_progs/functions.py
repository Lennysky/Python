f = open('my_file.txt', 'w')
f.write('Hi, my file!')
f.close()

# здесь нужно указать полный путь к файлу. Ща он у меня лежит там же, где и код
f = open('test for open.txt')
r = f.read()
print(r)

s= [354, 54, 556, 6878, 545, 55, 5]
print("Max: ", max(s))
print("Min: ", min(s))
print("Sum: ", sum(s))
print(list(range(0, 5)))
print("Sum: ", sum(list(range(0, 5))))

# Так выведет только вот такое: 
print (range (0, 10))

# Нужно превратить, например, в список:
print (list(range (0, 10, 2)))

for i in range(0,5):
    print(i)


sp = ["3df4", 5465, "654", "sdf"]
s = "This is my text!"
print(len(sp))


print ('введите ваш возраст: ')
age = input()
# нужно обязательно перевести в int, т.к. по умолчанию инпут принимает строку.
if int(age) > 10:
    print('Вам больше 10')

exec('''s = 10
b = 20
print (s+b)
''')



# выведет на экран текст
print ("Введите выражение:")
# считает то, что вводит пользовтель в переменную v
v = input()
# выведет на экарн результат: и выполнит выражение eval(v)
print("результат: ", eval(v))
