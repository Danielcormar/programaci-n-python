class Medico:
	def __init__(self,cod_medico,fecha,turnos_libres,turnos_ocupados):
		self.cod_medico=cod_medico
		self.fecha_atencion=fecha
		self.turnos_libres=turnos_libres
		self.turnos_ocupados=turnos_ocupados
class Agendas_medicas:
	def __init__(self,especialidad,fecha1,fecha2):
		self.especialidad=especialidad
		self.desde=fecha1
		self.hasta=fecha2
		self.agenda=[]
	def verificar_turno(self,medico,fecha):
		if any(medico==m.cod_medico for m in self.agenda):
			for m in self.agenda:
				if m.cod_medico==medico:
					if fecha>m.fecha_atencion and m.turnos_libres>0:
						return True
					else:
						return False
				else:
					pass
		else
			return False
