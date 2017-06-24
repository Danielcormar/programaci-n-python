class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

	def suma(self):
		return sum(self.items)

    def size(self):
        return len(self.items)
class Producto:
	def __init__(self,cod_producto,precio,fecha):
		self.cod_producto=cod_producto
		self.fecha=fecha
		self.precio=precio
		self.precios_ant=Queue()
	def remarcar(self,nuevoprecio,fecha)
		self.precios_ant.enqueue(self.precio)
		self.precio=nuevoprecio
		self.fecha=fecha
	def promedio(self):
		promedio=(float(self.precio+self.precios_ant.suma())/float(1+self.precios_ant.size()))
		return promedio
class Productos_remarcados:
	def __init__(self):
		self.productos=[]
	def agregar_producto(self,cod_producto,precio,fecha):
		self.productos.append(Producto(cod_producto,precio,fecha))
		self.productos=sorted(self.productos,key=lambda x: (x.cod_producto,x.precios_ant.size(),x.promedio()))
	def remaracar_producto(self,cod_producto,nuevoprecio,fecha):
		if any(i.cod_producto==cod_producto for i in self.productos):
			for pro in self.productos:
				if pro.cod_producto==cod_producto:
					pro.remarcar(nuevoprecio,fecha)
					return True
				else:
					pass
		else:
			return False
	def productos_mas_remarcados(self,n):
		productos_mas=[]
		for pro in self.productos:
			if pro.precios_ant.size()=>n:
				productos_mas.append(pro)
			else:
				pass
