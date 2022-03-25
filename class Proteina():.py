class Proteina():
	def _init_(self, clas, org, expr, muta):
		self.clasificacion = clas
		self.organismo = org
		self.expresion = expr
		self.mutacion = muta
		
	def mostrar_datos(self):	
		print(f"la clasificacion es {self.clasificaicon}, es un organismo {self.organismo}, con una sistema de expresion{self.expresion} y presenta mutacion {self.mutacion}")

proteina = Proteina("PROTEIN TRANSPORT", "Escherichia coli", "Escherichia coli", "No")		
proteina.mostrar_datos()