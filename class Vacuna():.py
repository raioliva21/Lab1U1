class Vacuna():
	def _init_(self, nombre, laboratorio):
		self.nombre = nombre
		self.laboratorio = laboratorio
		self.efectos = []
		 
	def agregar_efecto_secundario(self, efecto):
		self.efectos.append(efecto)
		
	
	def mostrar_efecto(self):
		for efecto in self.efectos:
			print(efecto)

vacuna1 = Vacuna("Pfizer", "Biontech")
vacuna2  = Vacuna("aperture", "Science")
vacuna3 = Vacuna("black", "mesa")

vacuna1.agregar_efecto_secundario('diarrea')
vacuna2.agregar_efecto_secundario('vomito')
vacuna3.agregar_efecto_secundario('colicos')

vacuna1.mostrar_efecto()
vacuna2.mostrar_efecto()
vacuna3.mostrar_efecto()