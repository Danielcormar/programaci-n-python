class Stack():
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)
class Tarea:
	def __init__(area,descripcion):
		self.area=area
		self.descripcion=descripcion
	def __repr__(self):
		return self.descripcion
class tareas_empleados:
	def __init__(self):
		self.lista_empleados=[]
	def agregar empleado(self):
		self.append(Stack())
	def agregar_tarea(self,tarea,descripcion):
		self.lista_empleados[self.lista_empleados.index(min(self.lista_empleados))].push(Tarea(area,descripcion))
	def procesar(self):
		for i in range(14,29):
			try:
				while self.lista_empleados[i].isEmpty()==False:
					t=self.lista_empleados[i].pop
					print 'Empleado '+str(i+1)+t
			except:
				print 'No hay mas empleados'
				return False
