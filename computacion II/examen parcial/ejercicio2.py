class Queue:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def enqueue(self, item):
		self.items.insert(0,item)
	def dequeue(self):
		return self.items.pop()
	def size(self):
		return len(self.items)
class Llamadas:
	def __init__(self,telefono,fecha,hora,destino,duracion,valor):
		self.telefono=telefono
		self.fecha=fecha
		self.hora=hora
		self.destino=destino
		self.duracion=duracion
		self.valor=valor
class Lista_de_llamadas:
	def  __init__(self):
		self.lista_de_llamadas_realizadas=Queue()
		self.lista_de_llamadas_facturadas=[]
	def facturar_llamadas_por_fecha(self,numTel,fechInicio,fechFinal):
		nueva_pila=Queue()
		for llamada in range(len(self.lista_de_llamadas_realizadas.size))
			llamada=self.lista_de_llamadas_realizadas.dequeue()
			if llamada.telefono==numTel:
				self.lista_de_llamadas_facturadas.append(llamada)
			else:
				nueva_pila.enqueue(a)
		self.lista_de_llamadas_realizadas=nueva_pila
	def llamadas_valorizadas(self):
		lista=[] #llamadas facturadas agrupadas por numero destino de la llamada
		destinos=[]
		for destino in self.lista_de_llamadas_facturadas:
			if destino.destino not in destinos:
				destino.append(destino.destino)
			else:
				pass
		destinos.sort()
		for destino in destinos:
			agrupar=[]
			for llamada in self.lista_de_llamadas_facturadas:
				if llamada.destino==destino:
					agrupar.append(llamada)
				else:
					pass
			lista.append(agrupar)
		return lista
	def agrgar_llamadas(self,telefono,fecha,hora,destino,duracion,valor):
		llamada=Llamadas(telefono,fecha,hora,destino,duracion,valor)
		self.lista_de_llamadas_realizadas.enqueue(llamada)
