for i in range (0, 5):
	print ("Hi %s" %i)
	print ("Hurrah!")

print (list(range(10,17)))

# 
sp1 = [10, 34, 45, 56, 88, 109, 345]

# 
sp2 = ["Привет", "Ура", "Мир", "Победа", "Да", "Уиии", "еее"]

# найденные монеты
found_coins = 20
# те, которые делает машина
magic_coins = 10
# ворует ворона
stolen_coins = 2

coins = found_coins
# сколько момент получится через год
print (found_coins + 365 * (magic_coins - stolen_coins))

for day in range (0, 365):
	coins = coins + magic_coins - stolen_coins
	print ("День %s: Стало монет %s" % (day, coins))