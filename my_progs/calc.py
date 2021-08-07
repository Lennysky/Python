print('Введите число а=')
a = int(input())
print('Введите число b=')
b = int(input())

print('Выберете операцию')
print('1 - сложить а+b')
print('2 - вычесть а-b')
d = int(input())

if d == 1:
    print('Сумма а + b = ', a+b)
    
if d == 2:
    print('Разность а - b = ', a-b)
