#Game tamagochi

name = input("Nama monster : ")
monster = {"name": name, 'power': 100}

def startGame():
	choice = input("Mau apa? 1.makan 2.lihat status 3.keluar")
	if choice == "1":
		goEat()
	elif choice == "2":
		goStatus()
	else :
		goExit()

def goEat():
	print("Kenyang....")
	monster['power'] += 100
startGame()


def goStatus():
	print("Cek dulu..")
	print(monster)
startGame()

def goExit():
	print("Bye Bye....")
startGame()