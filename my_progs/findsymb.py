str1 = 'Hello, World! This is me again!'

index = str1.find('This')
print(index)
index = str1.find('again')
print(index)


#Искать с определенной позиции:
index = str1.find('m', str1.find('This'), str1.find('again'))
print(index)

# Проверить, начинается ли наша строка с этой подстроки
yesno = str1.startswith("Hello")
print(yesno)

# startswith можно реализовать 1 в 1 через метод find:
print (str1.find("Hello")==0)

# заканчивается ли строка на нашу подстроку
yesno = str1.endswith("again!")
print(yesno)

# метод endswith можно тоже реализовать через find
#  если найдем подстроку "again" и оно будет равняться смещению len(str1)-len("again!"), будет true 
print (str1.find("again!")==len(str1)-len("again!"))