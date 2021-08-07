
print("Введите число а = ")
try:
    a = float (input())
    procent = 100 / a
    print("100/a = %s" % procent)

except ValueError:
    print ("Вы ввели не число")
except ZeroDivisionError:
    print ("Вы ввели ноль")
except:
    print ("Возникла ошибка!!! ")
# выполняется, если все хорошо и не было ошибок
else:
    print ("Все выполнилось без ошибок!")
# выполняется всегда: была ошибка или ее не было
finally:
    print ("Блок выполняется в любом случае")
    
