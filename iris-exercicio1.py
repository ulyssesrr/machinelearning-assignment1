import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from tabulate import tabulate

iris = datasets.load_iris()
matIris = iris.data
classes = iris.target_names

header = [" "] + iris.feature_names
data = []

globalMean = ["Média (Global)"] + np.mean(matIris, axis=0, dtype=np.float64).tolist()
data = data + [globalMean]

globalVariance = ["Variância (Global)"] + np.var(matIris, axis=0, dtype=np.float64).tolist()
data = data + [globalVariance]

idx = []
for i, val in enumerate(classes):
	cIdx = np.where(iris.target == i)[0].tolist()
	data += [[("Média (%s)" % val)] + np.mean(matIris[cIdx], axis=0, dtype=np.float64).tolist()]
	data += [[("Variância (%s)" % val)] + np.var(matIris[cIdx], axis=0, dtype=np.float64).tolist()]
	idx = idx + [cIdx]

print(tabulate(data, header, tablefmt="grid"))

#for i, val in enumerate(classes):
#	print("Matriz de Correlação: %s" % val)
#	print(tabulate(np.corrcoef(matIris[idx[i]])))

for j, nomeAtrib in enumerate(iris.feature_names):
	f, axArr = plt.subplots(1, len(classes), sharey=True)
	axArr[0].set_ylabel('Frequência')
	f.text(0.5, 0.975, nomeAtrib, horizontalalignment='center', verticalalignment='top')
	for i, nomeClasse in enumerate(classes):
		cMat = matIris[idx[i]][:,j]
		axArr[i].hist(cMat, bins=8, range=(0, np.amax(cMat)))
#		axArr[i].hist(cMat, bins=8)
		axArr[i].set_xlabel(("Iris %s" % nomeClasse))
		axArr[i].grid(True)

plt.show();



