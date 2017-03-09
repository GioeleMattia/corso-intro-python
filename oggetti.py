from datetime import datetime
import time

class Marca:
	def __init__(self, nome):
		self.nome = nome

	def __repr__(self):
		return "<Marca %s>" % self.nome

class Automobile:
	def __init__(self, name, anno, marca, consumo):
		self.nome = nome
		self.anno = anno
		self.carburante = 0
		self.consumo = int(consumo)
		self.marca = Marca(marca)
		self.eta = datetime.now().year - int(anno) 

	def __repr__(self):
		return "<Automobile %s>" % self.nome

	def rifornisci(self, litri):
		self.carburante += litri

	def consuma(self):
		self.carburante -= self.consumo

if __name__ == '__main__':
	nome = raw_input("Nome della macchina: ")
	anno = raw_input("Anno di fabbricazione (aaaa): ")
	marca = raw_input("Marca: ")
	consumo = raw_input("Consumo: ")

	while len(anno) != 4:
		print "Errore dnel formato dell'anno"
		anno = raw_input("anno di fabricazione (aaaa): ")
	
	mia_auto = Automobile(nome, anno, marca, consumo)
	
	print mia_auto
	print "Costruita nel %s" % mia_auto.anno
	print "Quindi ha %s" % mia_auto.eta
	
	print "Carburante: %s litri" % mia_auto.carburante
	mia_auto.rifornisci(30)
	print "Carburante: %s litri" % mia_auto.carburante

	secondi = 20
	while secondi > 0:
		mia_auto.consuma()
		
		if mia_auto.carburante <= 0:
			print "Finita la benza"
			break

		secondi -= 1
		time.sleep(1)
		print "Carburante: %s litri" % mia_auto.carburante


	print "Quindi possiedi una %s %s del %s" % (mia_auto.marca.nome, mia_auto.nome, mia_auto.anno)

