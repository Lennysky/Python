p = 100
def pab ():
        r = 10
        h = 20
        print (p, r, h)

pab()
print (r)      

def ploschad_axb (a, b):
	return a * b



def podschet_monet_i_ih_ves (monety, ves, nomer):
	print ("Подсчет № %s" % nomer)
	print ("Всего вес монет: %s" % (monety * ves))


podschet_monet_i_ih_ves (100, 2.5, 1)
podschet_monet_i_ih_ves (200, 5, 2) 

a1 = 100
b1 = 200


print ("Площадь прямоугольника %s на %s равна %s" % (a1, b1, ploschad_axb(a1, b1)))

for i in range (0,3):
	print ("Введите а: ")
	a = int(input ())
	print ("Введите b: ")
	b = int(input ())
	print ("Площадь прямоугольника %s на %s равна %s" % (a, b, ploschad_axb(a, b)))
