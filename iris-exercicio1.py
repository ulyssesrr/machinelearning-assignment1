#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import numpy as np
import pylab as plt
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
	f, axArr = plt.subplots(1, 1)
	f.canvas.set_window_title(nomeAtrib)
	axArr.set_ylabel('Frequência')
	axArr.set_xlabel(nomeAtrib)
	#f.text(0.5, 0.975, nomeAtrib, horizontalalignment='center', verticalalignment='top')
	cMat = []
	for i, nomeClasse in enumerate(classes):
		cMat += [matIris[idx[i]][:,j]]

	axArr.hist(cMat, bins=8, label=classes, alpha=0.5, stacked=True)
	#axArr.hist(cMat, bins=8, label=classes, alpha=0.5)
	axArr.legend()
	axArr.grid(True)

plt.show();



