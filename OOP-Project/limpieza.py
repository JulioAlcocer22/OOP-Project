
class Limpieza:

	def __init__(self):
		pass

	@staticmethod
	def test(arr):
		for i, entrada in enumerate(arr, start=1):
			print(f"arr[{i}] = {entrada}")


	@staticmethod
	def estadandarizarCadenas(s):
		cambios = (
			("á", "a"),
			("é", "e"),
			("í", "i"),
			("ó", "o"),
			("ú", "u"),
		)

		for a, b in cambios:
			s = s.replace(a, b).replace(a.upper(), b.upper())

		return s.upper()

	@staticmethod
	def duplicadosArreglo(arreglo):
		mi_arreglo_sin_duplicados = []

		for elemento in arreglo:
		    if elemento not in mi_arreglo_sin_duplicados:
		        mi_arreglo_sin_duplicados.append(elemento)

		return mi_arreglo_sin_duplicados