import datetime.date as fechas

def Transaccion:
	def __init__(self,id,fecha,numero_cta,monto,tipo):
		self.id=id
		self.fecha=fecha
		self.numero_cta=numero_cta
		self.monto=monto
		self.tipo=tipo

def registros:
	def __init__(self):
		self.lista=[]
		self.id=0
	def nueva_trans(self,self.id,fecha,numero_cta,monto,tipo):
		self.lista.append(Transaccion(self.id,fecha,numero_cta,monto,tipo))
		self.id=self.id+1
	def calcular_depositos(self):
		depositos=0
		fecha1=datetime.date(01,01,2004)
		fecha2=datetime.date(31,07,2004)
		for trans in self.lista:
			if trans.fecha>fecha1 and trans.fecha<fecha2:
				if trans.tipo=='deposito'
					depositos=depositos+1
				else:
					pass
			else:
				pass
		return depositos
	def total_depositado(self):
		total=0
		for trans in self.lista:
			if trans.fecha.year==2003:
				if trans.tipo=='deposito':
					total=total+trans.monto
				else:
					pass
			else:
				pass
		return total
	def calcular_saldo(self):
	saldo=0
	for trans in self.lista:
		if trans.numero_cta=='8894':
			if trans.fecha.year==2003:
				if trans.tipo=='deposito':
					saldo=saldo+trans.monto
				elif trans.tipo=='extraccion':
					saldo=saldo-trans.monto
				else:
					pass
			else:
				pass
		else:
			pass
	return saldo
	
