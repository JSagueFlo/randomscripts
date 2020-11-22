# IPC 3.8% ANUAL
# SOU ESTABLE 2020 = 2000€ MES = 24000€ ANUALS

def incrementAny(x):
	return round((x * 0.025), 2)


def calculaSetantaAnys(any_actual, souBase, souIncrementat, total):
	increment = incrementAny(souBase)
	souIncrementat = round(increment + souIncrementat, 2)
	total = round(total + souIncrementat, 2)
	any_actual = any_actual + 1
	print("Any {}\tEURAnual: {}€\tincrement: {}€\tEURAnualINC: {}€\ttotal: {}€".format(
		any_actual, souBase, increment, souIncrementat, total))
	souBase = souIncrementat
	if any_actual == 2080:
		return round(total, 2)
	else:
		return round(calculaSetantaAnys(
			any_actual, souBase, souIncrementat, total), 2)

any_actual = 2020
souBase = 1354 * 14
souIncrementat = souBase
total = souBase
print("Calcul del cost de la vida")
print("--------------------------")
print("Any {}\tEURAnual: {}€\tEURAnualINC: {}€\tEURAnualINC: {}€\ttotal: {}€".format(
	any_actual, souBase, souBase, souIncrementat, total))
supertotal = calculaSetantaAnys(any_actual, souBase, souIncrementat, total)

print()
print("+ 1 casa: {}€".format(500000))
print("+ 1 pis: {}€".format(150000))
print("+ 7 cotxes: {}€".format(20000 * 7))
print("supertotal: {}€".format(supertotal + 500000 + 150000 + 20000 * 7))